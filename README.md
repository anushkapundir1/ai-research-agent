# 🔍 AI Research Agent (RAG-Based)

🚀 An end-to-end **AI Research Agent** that performs real-time web research, semantic retrieval, and generates **structured, citation-backed reports** using **Retrieval-Augmented Generation (RAG)**.

Built using **FastAPI + Streamlit + LangChain + Groq LLM + ChromaDB**, this system enables users to query any topic and get accurate, source-grounded answers similar to Perplexity AI.

---

## 🔥 Highlights

- 🌐 Real-time web search using Tavily API  
- 🧠 Context-aware answers using RAG pipeline  
- 🔍 Semantic search using embeddings  
- ⚡ Fast retrieval using ChromaDB  
- 📊 Source-grounded responses with citations  
- 🎯 End-to-end pipeline (search → scrape → retrieve → generate)  


---

## 🧠 System Architecture (How it Works)

<div align="center">

<pre>
+----------------------+
|      User Query      |
+----------+-----------+
           |
           ▼
+----------------------+
|  Web Search (Tavily) |
+----------+-----------+
           |
           ▼
+---------------------------+
|      Web Scraping         |
|     (BeautifulSoup)       |
+----------+----------------+
           |
           ▼
+---------------------------+
| Text Chunking             |
| (Splitter)                |
+----------+----------------+
           |
           ▼
+---------------------------+
| Embeddings Generation     |
| (HuggingFace Model)       |
+----------+----------------+
           |
           ▼
+---------------------------+
|     Vector Database       |
|       (ChromaDB)          |
+----------+----------------+
           |
           ▼
+---------------------------+
| Similarity Retrieval      |
| (Top-K Relevant Chunks)   |
+----------+----------------+
           |
           ▼
+---------------------------+
|      LLM Processing       |
|     (Groq - LLaMA 3)      |
+----------+----------------+
           |
           ▼
+---------------------------+
|     Structured Output     |
|      + Citations          |
+---------------------------+
</pre>

</div>



---

## 🛠️ Tech Stack

| Category        | Tools Used                          |
|----------------|------------------------------------|
| Language       | Python                             |
| Backend        | FastAPI                            |
| Frontend       | Streamlit                          |
| LLM            | Groq (LLaMA 3)                     |
| Framework      | LangChain                          |
| Embeddings     | HuggingFace (Sentence Transformers)|
| Vector DB      | ChromaDB                           |
| Search API     | Tavily                             |
| Scraping       | BeautifulSoup                      |

---

## 📂 Project Structure

```bash
ai-research-agent/
│── app/
│   ├── main.py           # FastAPI backend
│   ├── search_tool.py    # Tavily search
│   ├── scraper.py        # Web scraping logic
│   ├── summarizer.py     # LLM response generation
│   ├── rag.py            # RAG pipeline (Chroma + retrieval)
│
│── streamlit_app.py      # Frontend UI
│── requirements.txt      # Dependencies
│── .env                  # API keys
```

---
## ⚙️ Installation & Setup
```bash
# 1. Clone repository
git clone https://github.com/anushkapundir1/ai-research-agent.git
```
```bash
# 2. Navigate to project
cd ai-research-agent
```
```bash
# 3. Create virtual environment
python -m venv venv
```
```bash
# 4. Activate environment
# Windows
venv\Scripts\activate
```
```bash
# Mac/Linux
source venv/bin/activate
```
```bash
# 5. Install dependencies
pip install -r requirements.txt
```
---

## 🔑 Environment Variables

### Create a .env file:
```bash
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
```
---
## ▶️ Running the Project
### Start Backend (FastAPI)
```bash
uvicorn app.main:app --reload
```
Docs:
http://127.0.0.1:8000/docs

### Start Frontend (Streamlit)
```bash

streamlit run streamlit_app.py
```
UI:
http://localhost:8501

---


## 💡 Example Use Cases
* 📊 Market & competitor research
* 🧠 AI-powered knowledge assistant
* 📚 Academic research summaries
* 📰 Real-time topic analysis
---

## 🚀 Key Implementation Details
* Implemented RAG pipeline for accurate, grounded responses
* Used text chunking for better embedding performance
* Designed multi-source retrieval strategy to improve diversity
* Integrated Groq LLM for fast inference
* Built full-stack system with FastAPI + Streamlit
  
---
## 📈 Future Improvements
* 💬 Conversational memory
* 🌐 Deployment on cloud
* 📄 Export reports (PDF)
* ⚡ Caching for faster responses
* 🔍 Hybrid search (keyword + vector)
---

### 🧪 Challenges Solved

- ❗ Preventing hallucination using RAG
- ❗ Handling noisy scraped web data
- ❗ Ensuring multi-source retrieval instead of single source dominance
- ❗ Managing latency in multi-step pipeline

---

## 👩‍💻 Author

Anushka Pundir
📧 anushkapundir70@gmail.com

--- 

## ⭐ Support

If you found this useful, consider giving it a ⭐ on GitHub!

---

## 🏷️ Tags

`#AI` `#RAG` `#FastAPI` `#LangChain` `#LLM` `#Python` `#GenerativeAI`
