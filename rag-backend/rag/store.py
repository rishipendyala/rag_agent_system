from qdrant_client import QdrantClient
from rag.embeddings import embed_text

client = QdrantClient(host="localhost", port=6333)

COLLECTION_NAME = "documents"

def setup_collection():
    """
    Set up the Qdrant collection for storing document embeddings.
    """
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config={
            "size": 384,  # Size of the embedding vectors from 'all-MiniLM-L6-v2'
            "distance": "Cosine"
        }
    )

def store_documents(documents):
    """
    Store documents and their embeddings in the Qdrant collection.
    
    documents : list of strings
    """
    points = []
    for idx, doc in enumerate(documents):
        vector = embed_text(doc)
        points.append({
            "id": idx,
            "vector": vector,
            "payload": {"text": doc}
        })
        
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )