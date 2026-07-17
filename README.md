# AI Resume Matcher

An AI-powered Resume Matcher built with Python that extracts text from resumes, parses resumes and job descriptions into structured Pydantic models using Groq LLM, and evaluates how well a candidate matches a job description.

This project was built as part of my AI Engineering learning journey with a focus on clean architecture, modular design, and production-ready software engineering practices.

---

## Features

### ✅ Implemented

- Extract text from PDF resumes
- Extract text from DOCX resumes
- Parse job descriptions using Groq Structured Outputs
- Parse resumes using Groq Structured Outputs
- Convert LLM responses into strongly typed Pydantic models
- AI-powered resume vs job matching
- Generate:
  - Match score
  - Matching skills
  - Missing skills
  - Experience evaluation
  - Education evaluation
  - Hiring recommendation

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
│   ├── match.py
│   └── __init__.py
│
├── services/
│   ├── extractor.py
│   ├── job_parser.py
│   ├── resume_parser.py
│   ├── matcher.py
│   └── __init__.py
│
├── resumes/
├── output/
└── README.md
```

---

## Application Workflow

```text
                 Resume PDF / DOCX
                        │
                        ▼
               Text Extraction
                        │
                        ▼
              Resume Parser (LLM)
                        │
                        ▼
               Resume Pydantic Model
                        │
                        │
                        │
Job Description ───────────────► Job Parser (LLM)
                        │
                        ▼
                Job Pydantic Model
                        │
                        ▼
                 AI Matching Engine
                        │
                        ▼
                 MatchResult Model
                        │
                        ▼
               Match Score & Verdict
```

---

## Example Output

```json
{
  "score": 70,
  "details": {
    "candidate_name": "Arnav Amrit",
    "matching_skills": [
      "...",
      "..."
    ],
    "missing_important_skills": [
      "...",
      "..."
    ],
    "experience_requirement_met": true,
    "education_requirement_met": true,
    "verdict": "..."
  }
}
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

Run the application:

```bash
python main.py
```

---

## Roadmap

### ✅ Phase 1 — Resume Extraction

- [x] PDF extraction
- [x] DOCX extraction

### ✅ Phase 2 — AI Parsing

- [x] Job parser
- [x] Resume parser

### ✅ Phase 3 — Matching Engine

- [x] Resume vs Job comparison
- [x] Match score generation
- [x] Missing skill analysis
- [x] Hiring recommendation

### 🚀 Future Improvements

- Streamlit UI
- FastAPI REST API
- Better Resume Models (Education, Projects)
- Strongly Typed MatchResult
- Shared LLM Client (`services/llm.py`)
- Prompt Templates
- Qdrant Integration
- Resume Embeddings
- Semantic Resume Search
- Multi-resume Ranking

---

## Software Engineering Principles

This project follows:

- Separation of Concerns (SoC)
- Single Responsibility Principle (SRP)
- Modular Architecture
- Pydantic Data Models
- Structured LLM Outputs
- Type Hints
- Environment Variables
- Incremental Git Workflow

---

## Learning Outcomes

Through this project, I learned:

- AI Engineering Fundamentals
- LLM Application Development
- Prompt Engineering
- Structured Outputs
- Pydantic
- JSON Schema
- Software Architecture
- Git & GitHub Workflow
- Modular Python Design

---

## License

This project is for educational and learning purposes.