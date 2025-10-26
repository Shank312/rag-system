
from pathlib import Path
from sentence_transformers import SentenceTransformer
import chromadb
from typing import List, Dict

MODEL_NAME = "all-MiniLM-L6-v2"

class Ingestor:
    def __init__(self, kb_path: str = "data/knowledge_base", persist_directory: str = None):
        self.kb_path = Path(kb_path)
        self.persist_directory = persist_directory
        # ✅ Use new Chroma client API
        if persist_directory:
            self.client = chromadb.PersistentClient(path=persist_directory)
        else:
            self.client = chromadb.EphemeralClient()
        self.embedding_model = SentenceTransformer(MODEL_NAME)

    def _load_documents(self) -> Dict[str, str]:
        docs = {}
        for p in self.kb_path.glob("*.md"):
            docs[p.name] = p.read_text(encoding="utf-8")
        return docs

    def _embed_texts(self, texts: List[str]):
        return self.embedding_model.encode(texts, show_progress_bar=True, convert_to_numpy=True)

    def ingest(self, collection_name="rag_kb"):
        docs = self._load_documents()
        if not docs:
            return {"ingested": 0, "ids": []}
        ids = list(docs.keys())
        texts = list(docs.values())
        embs = self._embed_texts(texts).tolist()
        try:
            self.client.delete_collection(collection_name)
        except Exception:
            pass
        col = self.client.create_collection(collection_name)
        col.add(ids=ids, documents=texts, embeddings=embs, metadatas=[{"source": i} for i in ids])
        return {"ingested": len(ids), "ids": ids}
