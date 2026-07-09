# Architecture

## Overview

The AI Teacher Assistant follows a modular Retrieval-Augmented Generation (RAG) architecture.

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

## Components

### Ingestion

Responsible for:

- Curriculum loading
- Metadata extraction
- Document chunking

### Retrieval

Responsible for:

- Query parsing
- Metadata filtering
- TF-IDF retrieval

### Generation

Responsible for:

- Grounded answer generation

### Evaluation

Responsible for:

- Retrieval evaluation metrics
- Automated testing