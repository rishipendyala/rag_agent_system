from qdrant_client import QdrantClient
from rag.embeddings import embed_text

client = QdrantClient(host="localhost", port=6333)
COLLECTION_NAME = "documents"

def retrieve_docs(query: str, limit: int = 3):
    vector = embed_text(query)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=vector,
        limit=limit
    )

    return [point.payload.get("text", "") for point in results.points]
