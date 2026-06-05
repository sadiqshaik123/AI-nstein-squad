# app.py
# Streamlit UI for AI Supplier Risk Platform

import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000"

st.set_page_config(
    page_title="AI Supplier Risk Dashboard",
    page_icon="⚠️",
    layout="wide"
)

# --------------------------
# API Helpers
# --------------------------

def get_dashboard():
    try:
        response = requests.get(
            f"{API_URL}/dashboard",
            timeout=30
        )
        return response.json()
    except Exception as e:
        st.error(f"Dashboard API Error: {e}")
        return {}

def get_supplier_risk(supplier):
    try:
        response = requests.post(
            f"{API_URL}/supplier-risk",
            json={"supplier": supplier},
            timeout=180
        )
        return response.json()
    except Exception as e:
        st.error(f"Supplier Analysis Error: {e}")
        return {}

def ask_chatbot(question):
    try:
        response = requests.post(
            f"{API_URL}/chat",
            json={"query": question},
            timeout=180
        )
        return response.json()
    except Exception as e:
        return {"response": str(e)}

# --------------------------
# Header
# --------------------------

st.title("⚠️ AI-Driven Supplier Risk Assessment")

st.markdown("""
### Integrated Agents

- Financial Agent (Bloomberg)
- News Agent (MCP)
- Compliance Agent (MCP)
- Logistics Agent (A2A)
- Social Media Agent
- Recommendation Agent
- Explanation Agent
""")

# --------------------------
# Dashboard
# --------------------------

dashboard = get_dashboard()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Suppliers",
        dashboard.get("total_suppliers", "-")
    )

with col2:
    st.metric(
        "High Risk",
        dashboard.get("high_risk_suppliers", "-")
    )

with col3:
    st.metric(
        "Critical",
        dashboard.get("critical_suppliers", "-")
    )

with col4:
    st.metric(
        "Alerts",
        dashboard.get("active_alerts", "-")
    )

# --------------------------
# Supplier Analysis
# --------------------------

st.divider()

supplier_name = st.text_input(
    "Supplier Name",
    placeholder="Enter Supplier Name"
)

if st.button("Analyze Supplier"):

    if supplier_name:

        with st.spinner(
            "Running Financial, MCP, A2A and Social Agents..."
        ):

            result = get_supplier_risk(
                supplier_name
            )

        risk_score = result.get(
            "risk_score",
            0
        )

        summary = result.get(
            "summary",
            "No summary generated"
        )

        c1, c2 = st.columns([1, 2])

        with c1:

            st.metric(
                "Risk Score",
                risk_score
            )

            if risk_score >= 80:
                st.error("CRITICAL")

            elif risk_score >= 60:
                st.warning("HIGH")

            elif risk_score >= 40:
                st.info("MEDIUM")

            else:
                st.success("LOW")

        with c2:
            st.subheader("AI Explanation")
            st.write(summary)

        st.divider()

        tabs = st.tabs(
            [
                "Financial",
                "News",
                "Compliance",
                "Logistics",
                "Social Media",
                "Recommendations"
            ]
        )

        with tabs[0]:
            st.json(
                result.get(
                    "financial_agent",
                    {}
                )
            )

        with tabs[1]:
            st.json(
                result.get(
                    "news_agent",
                    {}
                )
            )

        with tabs[2]:
            st.json(
                result.get(
                    "compliance_agent",
                    {}
                )
            )

        with tabs[3]:
            st.json(
                result.get(
                    "logistics_agent",
                    {}
                )
            )

        with tabs[4]:
            st.json(
                result.get(
                    "socialmedia_agent",
                    {}
                )
            )

        with tabs[5]:
            recommendations = result.get(
                "recommendations",
                []
            )

            if recommendations:
                for item in recommendations:
                    st.success(item)
            else:
                st.info("No recommendations available")

# --------------------------
# Chatbot
# --------------------------

st.divider()

st.subheader("🤖 Supplier Risk Assistant")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

question = st.chat_input(
    "Ask about suppliers, risks, compliance..."
)

if question:

    st.session_state.chat_history.append(
        ("user", question)
    )

    answer = ask_chatbot(question)

    st.session_state.chat_history.append(
        (
            "assistant",
            answer.get(
                "response",
                "No response"
            )
        )
    )

for role, msg in st.session_state.chat_history:

    with st.chat_message(role):
        st.write(msg)