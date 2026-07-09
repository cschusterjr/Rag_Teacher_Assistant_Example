# AI Teacher Assistant

## Project Goal

Build a curriculum-grounded Retrieval-Augmented Generation (RAG) application that demonstrates AI engineering, software engineering, data science, and product thinking.

The application allows teachers to ask questions about curriculum documents and receive grounded responses based on retrieved instructional content.

---

# Current Architecture

Teacher Question
↓
FastAPI API
↓
Query Parser
↓
Metadata Extraction
↓
Metadata Filtering
↓
Chunk Retrieval (TF-IDF)
↓
Answer Generation
↓
API Response

---

# Technical Stack

## Backend

- Python
- FastAPI

## Retrieval

- TF-IDF
- cosine similarity
- chunk-based retrieval

## Data Processing

- Markdown curriculum documents
- metadata extraction
- document chunking

## Testing

- pytest
- unit tests
- integration tests

---

# Features Completed

- Curriculum ingestion
- Automatic curriculum loading
- Chunking
- Metadata extraction
- Metadata-aware retrieval
- Query parser
- Answer generation
- Evaluation metrics
- Curriculum corpus
- Unit tests
- Integration tests

---

# Future Improvements

## Retrieval

- Embedding search
- Hybrid retrieval
- Reranking

## AI

- LLM-generated answers
- Conversation memory
- Lesson planning
- Parent communication generation

## Engineering

- Docker
- GitHub Actions
- Authentication

---

# Lessons Learned

(To be completed during project review.)