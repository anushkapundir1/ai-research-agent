from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

def summarize(topic, text):

    if not text:
        return "No text available for summarization."

    prompt = f"""
    Research topic: {topic}

    Context:
    {text}

    Write a research summary with key insights.
    """

    response = llm.invoke(prompt)

    return response.content