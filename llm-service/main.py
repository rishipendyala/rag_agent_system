from fastapi import FastAPI

app = FastAPI()

@app.post("/generate")
def generate_text(request: dict):
    prompt = request.get("prompt", "")
    return {
        "output": f"[LLM OUTPUT] Generated text for: {prompt}"
    }
