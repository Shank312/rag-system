
import chromadb
from sentence_transformers import SentenceTransformer
import numpy as np

MODEL_NAME = "all-MiniLM-L6-v2"

class Retriever:
    def __init__(self, chroma_client=None, collection_name="rag_kb"):
        self.client = chroma_client if chroma_client else chromadb.EphemeralClient()
        self.collection = self.client.get_collection(collection_name)
        self.embed_model = SentenceTransformer(MODEL_NAME)

    def retrieve(self, query: str, k: int = 3):
        q_emb = self.embed_model.encode([query], convert_to_numpy=True)[0].tolist()
        res = self.collection.query(query_embeddings=[q_emb], n_results=k, include=["documents","metadatas","distances","ids"])
        ids = res.get("ids", [[]])[0]
        docs = res.get("documents", [[]])[0]
        dists = res.get("distances", [[]])[0] if "distances" in res else []
        hits = []
        for i, doc in enumerate(docs):
            score = 1 - (dists[i] if i < len(dists) else 1.0)
            hits.append({"id": ids[i] if i < len(ids) else None, "document": doc, "score": score})
        return hits
