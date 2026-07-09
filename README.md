# AI Teacher Assistant

A curriculum-grounded **Retrieval-Augmented Generation (RAG)** application built to demonstrate modern AI engineering, software architecture, data science, and product thinking.

This project simulates an AI assistant that helps teachers retrieve curriculum information by combining structured metadata, document chunking, retrieval, and grounded answer generation.

---

# Why I Built This

Many AI chatbot demos focus only on connecting an LLM to a collection of documents.

I wanted to build something that demonstrates the engineering that happens **before** an LLM generates an answer.

The focus of this project is building a modular retrieval pipeline that can eventually support:

- Curriculum Q&A
- Lesson planning
- Parent communication
- Teacher support workflows

Rather than relying on proprietary curriculum, this project uses an original curriculum corpus created specifically for portfolio purposes.

---

# Architecture

```text
Teacher Question
        │
        ▼
FastAPI API
        │
        ▼
Query Parser
        │
        ▼
Metadata Extraction
        │
        ▼
Metadata Filtering
        │
        ▼
Chunk-Based Retrieval (TF-IDF)
        │
        ▼
Answer Generation
        │
        ▼
Grounded API Response
```

---

# Features

## Curriculum Processing

- Automatic curriculum loading
- Markdown-based curriculum documents
- Curriculum metadata extraction
- Document chunking

---

## Retrieval

- TF-IDF retrieval
- Metadata-aware retrieval
- Grade filtering
- Subject filtering
- Chunk-based search

---

## AI Pipeline

- Modular retrieval pipeline
- Query parsing
- Answer generation layer
- Retrieval evaluation metrics

---

## Software Engineering

- Modular architecture
- Unit tests
- Integration tests
- Clean project organization
- Automated curriculum loading

---

# Technology Stack

| Area | Technology |
|------|------------|
| Language | Python |
| API | FastAPI |
| Retrieval | scikit-learn TF-IDF |
| Testing | pytest |
| Data | Markdown curriculum corpus |
| Search | Cosine Similarity |

---

# Repository Structure

```text
app/
│
├── ingestion/
│   ├── chunking.py
│   ├── loader.py
│   └── metadata.py
│
├── retrieval/
│   ├── query_parser.py
│   ├── rag.py
│   └── store.py
│
├── generation/
│   └── generator.py
│
├── evaluation/
│   └── metrics.py
│
└── main.py

data/
└── curriculum/

tests/

docs/
```

---

# Example Workflow

1. Curriculum documents are loaded automatically.
2. Metadata is extracted.
3. Documents are chunked.
4. Chunks are indexed using TF-IDF.
5. Teacher submits a question.
6. Query parser extracts structured filters.
7. Matching curriculum is retrieved.
8. Grounded response is generated.

---

# Current Curriculum Corpus

The repository currently contains original curriculum documents covering:

- Grade 4 Mathematics
- Grade 5 Mathematics
- Grade 5 English Language Arts
- Grade 5 Science
- Grade 5 Social Studies
- Grade 6 Mathematics
- Grade 6 English Language Arts
- Grade 6 Science
- Grade 6 Social Studies

These documents were created specifically for this portfolio project and follow a standardized curriculum schema.

---

# Evaluation

The project includes automated testing for:

- Document chunking
- Metadata extraction
- Curriculum loading
- Query parsing
- Retrieval behavior
- Answer generation
- Evaluation metrics
- Integration testing

Current status:

**16 automated tests passing**

---

# Design Decisions

Some intentional architectural decisions include:

- Separate ingestion, retrieval, generation, and evaluation into independent modules.
- Use metadata filtering before retrieval.
- Build retrieval using TF-IDF before introducing embeddings.
- Create original curriculum documents instead of using copyrighted instructional materials.
- Build and test components independently before integration.

---

# Future Roadmap

Version 2 ideas include:

- Embedding-based retrieval
- Hybrid retrieval
- LLM integration
- Teacher lesson planning
- Parent communication generation
- HTML interface
- Docker deployment
- GitHub Actions CI/CD
- Evaluation dashboard

---

# About This Portfolio Project

This repository was built as part of my AI engineering portfolio to demonstrate skills across:

- AI Engineering
- Software Engineering
- Data Science
- Backend Development
- Product Architecture
- Educational Technology

The emphasis is on building maintainable AI systems with thoughtful architecture rather than simply integrating an LLM.