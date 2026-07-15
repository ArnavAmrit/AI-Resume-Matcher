# AI Resume Matcher

An AI-powered Resume Matcher built with Python that extracts resume data, structures it using LLMs, and compares candidate profiles against job requirements.

This project is being developed as part of my AI Engineering learning journey with a strong focus on software engineering principles, modular architecture, and production-ready code.

---

## Features

### Current
- Extract text from PDF resumes
- Extract text from DOCX resumes
- Modular project architecture
- Built using `uv` package management

### Planned
- Parse resumes using Groq LLM
- Structured Outputs with Pydantic
- Export structured JSON
- Skill matching against job descriptions
- Match percentage calculation
- AI-generated hiring recommendation
- RAG integration with Qdrant (future)

---

## Project Structure

```text
AI-Resume-Matcher/
│
├── config.py              # Project configuration
├── main.py                # Application entry point
├── pyproject.toml
├── uv.lock
│
├── models/                # Pydantic models
│
├── services/
│   └── extractor.py       # PDF/DOCX text extraction
│
├── resumes/               # Local resumes (ignored by Git)
├── output/                # Generated outputs
└── README.md
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

Create the virtual environment:

```bash
uv venv
```

Install dependencies:

```bash
uv sync
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## Roadmap

- [x] Project initialization
- [x] Resume text extraction (PDF/DOCX)
- [ ] Resume parsing using Groq
- [ ] Structured Outputs with Pydantic
- [ ] JSON export
- [ ] Resume-job matching
- [ ] AI recommendation
- [ ] RAG with Qdrant

---

## Learning Goals

This project emphasizes:

- Modular software architecture
- Separation of concerns
- Single Responsibility Principle (SRP)
- Type-safe data models with Pydantic
- Clean Git workflow
- Production-ready Python practices

---

## License

This project is created for learning and educational purposes.