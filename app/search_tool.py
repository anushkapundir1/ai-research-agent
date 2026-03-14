from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv
import os

load_dotenv("app/.env")

def search_web(query):

    tool = TavilySearchResults(max_results=5)

    results = tool.invoke(query)

    urls = []

    for r in results:
        if "url" in r:
            urls.append(r["url"])

    return urls