from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "The RAG backend is alive!"}

@app.post("/ask")
def ask_question(request: dict):
    query = request.get("query", "")
    return {"answer": f"You asked: {query}. Real AI is coming soon!"}