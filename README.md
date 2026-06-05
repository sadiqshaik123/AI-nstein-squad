# AI-nstein-squad

supplier-risk-poc/
│
├── app.py                      # Streamlit Dashboard + Chatbot
├── requirements.txt
├── README.md
│
├── config/
│   └── settings.py
│
├── api/
│   └── main.py                 # FastAPI
│
├── agents/
│   ├── supervisor.py           # LangGraph Supervisor
│   ├── mcp_agent.py
│   ├── kaggle_agent.py
│   ├── news_agent.py
│   ├── a2a_agent.py
│   ├── risk_agent.py
│   └── explanation_agent.py
│
├── mcp_server/
│   └── supplier_server.py
│
├── data/
│   ├── suppliers.csv
│   ├── kaggle_risk.csv
│   └── news.csv
│
└── vector_store/
    └── build_vector_db.py
