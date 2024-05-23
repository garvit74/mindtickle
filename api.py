from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from pinecone import Pinecone, ServerlessSpec
from llm_utils import encode_text, preprocess_query_with_llm
from config import PINECONE_API_KEY
from PyPDF2 import PdfReader
from document_cleaner import clean_text


pc = Pinecone(api_key=PINECONE_API_KEY)

# Create Pinecone index if it doesn't exist
index_name = 'mindtickle'
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,
        metric='cosine',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )

index = pc.Index(index_name)

app = FastAPI()


def extract_text_from_file(file_path, file_extension):
    text = ""
    if file_extension == "pdf":
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text()
    elif file_extension == "txt":
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        raise HTTPException(status_code=400, detail="Unsupported file format")
    return text


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Save the uploaded file
        file_extension = file.filename.split(".")[-1].lower()
        file_path = f"uploads/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())

        # Extract and clean text from the file
        text = extract_text_from_file(file_path, file_extension)
        cleaned_text = clean_text(text)

        # Generate embeddings and store in Pinecone
        embedding = encode_text(cleaned_text)
        index.upsert([(file.filename, embedding)])

        return {"filename": file.filename}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


@app.get("/search")
async def search_docs(q: str):
    try:
        # Preprocess query and generate embedding
        preprocessed_query = preprocess_query_with_llm(q)
        query_embedding = encode_text(preprocessed_query)

        # Query Pinecone for relevant documents
        results = index.query(vector=query_embedding, top_k=5, include_values=False)
        document_names = [result['id'] for result in results['matches']]

        return {"documents": document_names}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
