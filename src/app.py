
from fastapi import FastAPI
from pydantic import BaseModel
import chromadb
from src.ingest import Ingestor
from src.retriever import Retriever
from src.generator import Generator

app = FastAPI()
class QueryRequest(BaseModel):
    query: str

PERSIST_DIR = "chromadb_store"

try:
    client = chromadb.PersistentClient(path=PERSIST_DIR)
    try:
        client.get_collection("rag_kb")
    except Exception:
        Ingestor("data/knowledge_base", persist_directory=PERSIST_DIR).ingest("rag_kb")
except Exception:
    client = chromadb.EphemeralClient()
    Ingestor("data/knowledge_base", persist_directory=None).ingest("rag_kb")

retriever = Retriever(chroma_client=client)
generator = Generator()

@app.post("/query")
def query(req: QueryRequest):
    hits = retriever.retrieve(req.query)
    ans = generator.generate(req.query, hits)
    return {"query": req.query, "answer": ans, "retrieved": hits}
