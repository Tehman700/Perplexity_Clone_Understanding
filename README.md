# Purplexity.ai

A Perplexity.ai clone built from scratch. The backend is written manually with full understanding of every line — no vibe coding. The frontend is vibe coded.

This project exists solely to grasp backend concepts and to understand how things connect — web scraping, LLM pipelines, streaming, APIs — without blindly generating code.

---

## Tech Stack

**Backend**
- Python + FastAPI
- DuckDuckGo Search (`ddgs`) — web search without an API key
- Trafilatura — HTML content extraction
- Requests — HTTP fetching
- Tavily API — alternative search with richer results
- Pydantic — request validation
- python-dotenv — environment variable management
- Uvicorn — ASGI server

**Frontend**
- React + TypeScript
- Vite

---

## Features

- Query input that sends a POST request to the backend
- DuckDuckGo web search on the backend from a raw query
- Page content extraction — strips HTML, pulls clean body text
- Structured source output per result (title, URL, snippet, content)
- Tavily-powered search endpoint as an alternative pipeline
- CORS configured for local frontend-backend communication
- Environment-based API key management via `.env`

---

## Project Structure

```
Purplexity.ai/
├── backend/
│   ├── main.py        # FastAPI app, search pipeline, LLM endpoint
│   └── .venv/         # Python virtual environment (not committed)
├── frontend/
│   └── src/
│       ├── App.tsx
│       ├── App.css
│       └── index.css
├── .env               # API keys (not committed)
├── .gitignore
└── README.md
```

---

## Running Locally

**Backend**
```bash
cd backend
.venv\Scripts\activate
uvicorn main:app --reload
```
Runs on `http://localhost:8000`

**Frontend**
```bash
cd frontend
npm run dev
```
Runs on `http://localhost:5173`

Create a `.env` file at the project root:
```
TAVILY_API_KEY=your_key_here
```
