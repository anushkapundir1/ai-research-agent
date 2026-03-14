from fastapi import FastAPI
from app.search_tool import search_web
from app.scraper import scrape_page
from app.summarizer import summarize

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Research Agent Running"}

@app.get("/research")
def research(query: str):
    try:
        urls = search_web(query)

        documents = []

        for url in urls:
            text = scrape_page(url)

            if text:
                documents.append(text)

        if len(documents) == 0:
            return {
                "topic": query,
                "report": "No content could be extracted from the web.",
                "sources": urls
            }

        combined_text = " ".join(documents)

        report = summarize(query, combined_text)

        return {
            "topic": query,
            "report": report,
            "sources": urls
        }

    except Exception as e:
        print("ERROR:", e)
        return {"error": str(e)}