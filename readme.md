# Semantic Search Application with FastAPI, Transformers, and Pinecone
This repository implements a document processing and search application using FastAPI, Transformers, and Pinecone. It allows users to upload documents and then search for relevant content within those documents. Sentence embeddings are generated for both documents and queries to enable semantic similarity search using Pinecone.

# Features:

1. Uploads documents (Text or PDF).
2. Extracts text from uploaded documents.
3. Generates sentence embeddings for processed text.
4. Utilizes Pinecone for document storage and semantic search (Limited Functionality).
5. Provides a user-friendly API for uploading documents and searching content.

# Requirements:

* Python 3.x
* pip
* transformers
* sentence-transformers
* pinecone-client

# Installation:

## Clone this repository:

[https://github.com/garvit74/mindtickle](https://github.com/garvit74/mindtickle.git)
## Navigate to the project directory:

cd mindtickle


## Install the required dependencies:

pip install -r requirements.txt

## Usage:

## Set Up Pinecone:

* Create a Pinecone account and obtain your API key.
* Update the config.py file (if it exists) with your Pinecone API key.

## Start the application:

uvicorn main:app --host 0.0.0.0 --port 8000

* This will start the FastAPI server on port 8000.

## Upload documents:
Use a tool like Postman or curl to send a POST request to the appropriate endpoint for uploading documents:

/upload for PDF and text documents (with the document file in the file field).


## Search documents:
Send a GET request to the /search endpoint with the search query as a parameter named q.

## Current Functionality:

* Uploads and processes HTML and PDF documents.
* Generates sentence embeddings for extracted text.
* Stores document embeddings in Pinecone (Limited Search Functionality).


## Functionality in Progress:

Pinecone is currently not fully integrated for semantic search. You'll need to implement the logic to search for documents based on the query embedding in Pinecone.


## Deployment:

This application is deployed on Render.

## Contributing:

We welcome contributions to this project! Please create a pull request with your changes.
