from fastapi import FastAPI
import requests
from rag.store import setup_collection, store_documents


app = FastAPI()

LLM_SERVICE_URL = "http://127.0.0.1:8001/generate"

@app.get("/")
def root():
    return {"message": "The RAG backend is alive!"}

@app.on_event("startup")
def startup_event():
    setup_collection()
    store_documents([
        "RAG stands for Retrieval Augmented Generation.",
        "Microservices split systems into independent services.",
        "Vector databases store embeddings for similarity search.",
        "LLMs generate text based on prompts."
    ])
    
from rag.retrieve import retrieve_docs

@app.post("/ask")
def ask_question(request: dict):
    query = request.get("query", "")

    docs = retrieve_docs(query)
    context = "\n".join(docs)

    prompt = f"""
Use the context below to answer the question.

Context:
{context}

Question:
{query}
"""

    response = requests.post(
        LLM_SERVICE_URL,
        json={"prompt": prompt}
    )

    return {
        "answer": response.json()["output"],
        "context_used": docs
    }


