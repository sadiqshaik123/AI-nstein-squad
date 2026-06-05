# Supplier Risk Assessment POC

## Architecture
- Streamlit Dashboard + Chatbot
- FastAPI Backend
- LangGraph-style Supervisor (simplified POC)
- FastMCP Supplier Agent
- Kaggle Risk Agent (CSV based)
- Reuters/Bloomberg Agent (mocked news retrieval)
- A2A Agent (mocked logistics/weather)
- GenAI Lab LLM integration

## Run

```bash
pip install -r requirements.txt
python mcp_server/supplier_server.py
uvicorn api.main:app --reload
streamlit run app.py
```

## Configure GenAI Lab
Update config/settings.py with your API key.


https://chatgpt.com/gg/v/6a226e98fe4481a09a3092865bc73e3e?token=Wx-fDYf50autMiJGuSqPQQ
