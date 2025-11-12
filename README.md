# RAG Teacher Assistant

A simple Retrieval-Augmented Generation (RAG) microservice scaffold for answering curriculum questions from a small set of documents.

## Tech
- Python, FastAPI
- Local embeddings/vector store (duckdb + sqlite fallback for demo)
- Simple evaluation harness (precision@k placeholder)

## Getting Started
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Project Structure
```
app/
  main.py
  rag.py
  store.py
data/sample_docs/
tests/
```

## API
- `POST /ingest` — upload plain-text docs
- `POST /query` — ask a question, returns top-k passages
