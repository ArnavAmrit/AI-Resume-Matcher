# AI Resume Matcher

An AI-powered Resume Matcher built with Python that extracts resume information, parses job descriptions using Groq Structured Outputs, and will eventually compare candidate resumes against job requirements using AI.

This project is part of my AI Engineering learning journey, with a focus on clean architecture, modular design, and production-ready software engineering practices.

---

## Features

### ✅ Implemented

- Extract text from PDF resumes
- Extract text from DOCX resumes
- Parse job descriptions using Groq LLM
- Generate structured JSON using Pydantic JSON Schema
- Convert LLM responses into strongly typed Pydantic models
- Modular architecture following Separation of Concerns

### 🚧 Coming Next

- Resume parsing using Groq
- Resume Pydantic model
- Resume JSON export
- Resume vs Job skill matching
- Match percentage calculation
- AI hiring recommendation
- RAG integration with Qdrant
- Vector search for semantic resume matching

---

## Project Structure

```text
AI-Resume-Matcher/
│
├── config.py                  # Project configuration
├── main.py                    # Application entry point
├── pyproject.toml
├── uv.lock
│
├── models/
│   ├── job.py                 # Job description Pydantic model
│   └── __init__.py
│
├── services/
│   ├── extractor.py           # PDF/DOCX text extraction
│   ├── parser.py              # Groq job description parser
│   └── __init__.py
│
├── resumes/                   # Local resumes (ignored by Git)
├── output/
└── README.md
```

---

## Current Architecture

```text
                Resume
                   │
                   ▼
          Text Extraction
                   │
                   ▼
             Raw Resume Text
                   │
                   ▼
      (Resume Parser - Coming Next)

Job Description
        │
        ▼
 Groq Structured Outputs
        │
        ▼
      Pydantic Model
        │
        ▼
    Structured Job Data
```

---

## Tech Stack

- Python 3.13
- uv
- Groq API
- Pydantic
- pypdf
- python-docx
- python-dotenv

---

## Setup

Clone the repository:

```bash
git clone <repository-url>
cd AI-Resume-Matcher
```

Create a virtual environment:

```bash
uv venv
```

Install dependencies:

```bash
uv sync
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
```

Run the project:

```bash
python main.py
```

---

## Roadmap

### Phase 1 — Data Extraction

- [x] Project initialization
- [x] PDF text extraction
- [x] DOCX text extraction

### Phase 2 — AI Parsing

- [x] Job Description parser
- [ ] Resume parser
- [ ] JSON export

### Phase 3 — Resume Matching

- [ ] Skill matching
- [ ] Match percentage
- [ ] AI recommendation

### Phase 4 — Retrieval-Augmented Generation (RAG)

- [ ] Qdrant vector database
- [ ] Resume embeddings
- [ ] Semantic search
- [ ] Context-aware recommendations

---

## Software Engineering Principles

This project is intentionally designed using:

- Separation of Concerns
- Single Responsibility Principle (SRP)
- Modular Architecture
- Interface-first Design
- Pydantic Data Models
- Structured LLM Outputs
- Incremental Git Commits
- Type Hints

---

## Learning Goals

This project is helping me learn:

- AI Engineering
- LLM Application Development
- Structured Outputs
- Prompt Engineering
- Pydantic
- Software Architecture
- Git Workflow
- Production-ready Python

---

## License

This project is for educational and learning purposes.