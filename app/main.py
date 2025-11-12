from fastapi import FastAPI, UploadFile, File, Form
from typing import List
from .rag import RAGPipeline

app = FastAPI(title="RAG Teacher Assistant")
rag = RAGPipeline()

@app.post("/ingest")
async def ingest(docs: List[UploadFile]):
    texts = []
    for f in docs:
        texts.append((f.filename, (await f.read()).decode("utf-8", errors="ignore")))
    rag.ingest(texts)
    return {"status": "ok", "ingested": len(texts)}

@app.post("/query")
async def query(q: str = Form(...), k: int = Form(3)):
    results = rag.search(q, k=k)
    return {"query": q, "results": results}
