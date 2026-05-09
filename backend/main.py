from fastapi import FastAPI
import random
import os
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ddgs import DDGS
import trafilatura
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class SearchRequest(BaseModel):
    query: str

def search_web(query: str, max_results: int = 20):
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=max_results)
        return [{"title": r["title"], "url": r["href"], "snippet": r["body"]} for r in results]


def extract_content(url: str):
    try:
        response = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
        content = trafilatura.extract(response.text, include_comments=False, include_tables=False)
        return content or ""
    except Exception:
        return ""


@app.get("/api/ping")
def home():
    number = random.randint(1, 1000)
    return {"message": number}


@app.post("/conversation")
def conversation(body: SearchRequest):
    query = body.query

    print(f"\n{'='*50}")
    print(f"Query: {query}")
    print(f"{'='*50}")

    # Step 1: get urls and snippets from duckduckgo
    search_results = search_web(query)

    # Step 2: fetch and extract clean content from each url
    sources = []
    for result in search_results:
        content = extract_content(result["url"])
        sources.append({
            "title": result["title"],
            "url": result["url"],
            "snippet": result["snippet"],
            "content": content[:1000] if content else "Could not extract content"
        })

    # Step 3: print clean structured output
    for i, source in enumerate(sources, 1):
        print(f"\nSource {i}: {source['title']}")
        print(f"URL: {source['url']}")
        print(f"Snippet: {source['snippet']}")
        print(f"Content:\n{source['content']}")
        print(f"{'-'*40}")

    return {"status": "ok"}


# To install: pip install tavily-python
from tavily import TavilyClient
client = TavilyClient(os.getenv("TAVILY_API_KEY"))

@app.post("/conversation_tavily")
def conversation_tavily(body: SearchRequest):
    main_query = body.query
    response = client.search(
        query=main_query,
        search_depth="advanced"
    )
    return response
