from transformers import pipeline
from sentence_transformers import SentenceTransformer


# Initialize the models
query_preprocessor = pipeline('ner', model='dslim/bert-base-NER')
embedder = SentenceTransformer('all-MiniLM-L6-v2')


def preprocess_query_with_llm(query):
    entities = query_preprocessor(query)
    predicted_entities = [entity['word'] for entity in entities]

    if predicted_entities:
        preprocessed_query = f"{query} with entities: {', '.join(predicted_entities)}"
    else:
        preprocessed_query = query

    return preprocessed_query


def encode_text(text: str):
    embeddings = embedder.encode(text)
    return embeddings.tolist()
