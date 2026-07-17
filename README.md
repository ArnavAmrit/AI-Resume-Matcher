# AI Resume Matcher

An AI-powered Resume Matcher built with Python that extracts resume information, parses both resumes and job descriptions using Groq Structured Outputs, and will eventually compare candidates against job requirements using AI.

This project is part of my AI Engineering learning journey, focusing on clean architecture, modular design, and production-ready software engineering practices.

---

## Features

### ✅ Implemented

- Extract text from PDF resumes
- Extract text from DOCX resumes
- Parse job descriptions into structured Pydantic models
- Parse resumes into structured Pydantic models
- Generate structured JSON using Groq Structured Outputs
- Convert LLM responses into strongly typed Pydantic models
- Modular architecture following Separation of Concerns (SoC)

### 🚧 Coming Next

- Resume vs Job matching
- Skill similarity scoring
- Match percentage calculation
- AI hiring recommendation
- Resume ranking
- RAG integration with Qdrant
- Semantic search using vector embeddings

---

## Project Structure

```text
AI-Resume-Matcher/
│
├── config.py
├── main.py
├── pyproject.toml
├── uv.lock
│
├── models/
│   ├── job.py
│   ├── resume.py
│   └── __init__.py
│
├── services/
│   ├── extractor.py
│   ├── parser.py
│   ├── resume_parser.py
│   └── __init__.py
│
├── resumes/
├── output/
└── README.md
```

---

## Current Architecture

```text
                 Resume PDF / DOCX
                         │
                         ▼
                Text Extraction
                         │
                         ▼
                  Raw Resume Text
                         │
                         ▼
                 Resume Parser (LLM)
                         │
                         ▼
                  Resume Pydantic Model


                Job Description Text
                         │
                         ▼
                   Job Parser (LLM)
                         │
                         ▼
                   Job Pydantic Model
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

```bash
git clone <repository-url>
cd AI-Resume-Matcher

uv venv
uv sync
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
```

Run:

```bash
python main.py
```

---

## Roadmap

### Phase 1 — Extraction

- [x] Project setup
- [x] PDF extraction
- [x] DOCX extraction

### Phase 2 — AI Parsing

- [x] Job description parser
- [x] Resume parser

### Phase 3 — Matching Engine

- [ ] Resume vs Job comparison
- [ ] Skill matching
- [ ] Experience matching
- [ ] Match percentage
- [ ] AI recommendation

### Phase 4 — Retrieval-Augmented Generation (RAG)

- [ ] Resume embeddings
- [ ] Qdrant integration
- [ ] Semantic search
- [ ] Context-aware recommendations

---

## Software Engineering Principles

- Separation of Concerns (SoC)
- Single Responsibility Principle (SRP)
- Modular Architecture
- Pydantic Data Models
- Structured LLM Outputs
- Type Hints
- Incremental Git Workflow

---

## Learning Goals

This project is helping me learn:

- AI Engineering
- LLM Application Development
- Prompt Engineering
- Structured Outputs
- Pydantic
- Software Architecture
- Production-ready Python
- Git Best Practices

---

## License

This project is for educational and learning purposes.