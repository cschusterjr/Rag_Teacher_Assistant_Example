from fastapi import FastAPI, UploadFile, File, Form
from typing import List
from .generation.generator import generate_answer
from .retrieval.rag import RAGPipeline
from .ingestion.loader import load_curriculum_documents

app = FastAPI(title="RAG Teacher Assistant")
rag = RAGPipeline()

curriculum_docs = load_curriculum_documents("data/curriculum")
rag.ingest(curriculum_docs)

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

    answer = generate_answer(q, results)

    return {
        "question": q,
        "answer": answer,
        "sources": results,
    }
