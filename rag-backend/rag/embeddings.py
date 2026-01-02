from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_text(text):
    """
    Embed text into vectors using a pre-trained SentenceTransformer model.
    """
    vector = model.encode(text)
    return vector.tolist()



