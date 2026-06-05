# api/main.py
# FastAPI Backend for AI Supplier Risk Assessment Platform

from fastapi import FastAPI
from pydantic import BaseModel

from agents.financial_agent import FinancialAgent
from agents.news_agent import NewsAgent
from agents.compliance_agent import ComplianceAgent
from agents.logistics_agent import LogisticsAgent
from agents.socialmedia import SocialMediaAgent
from agents.risk_scoring_agent import RiskScoringAgent
from agents.recommendation_agent import RecommendationAgent
from agents.explanation_agent import ExplanationAgent

app = FastAPI(
    title="AI Supplier Risk Assessment API",
    version="1.0.0"
)

# -----------------------------
# Initialize Agents
# -----------------------------

financial_agent = FinancialAgent()
news_agent = NewsAgent()
compliance_agent = ComplianceAgent()
logistics_agent = LogisticsAgent()
social_agent = SocialMediaAgent()

risk_agent = RiskScoringAgent()
recommendation_agent = RecommendationAgent()
explanation_agent = ExplanationAgent()

# -----------------------------
# Request Models
# -----------------------------

class SupplierRequest(BaseModel):
    supplier: str
    country: str | None = None
    location: str | None = None


class ChatRequest(BaseModel):
    query: str


# -----------------------------
# Health Check
# -----------------------------

@app.get("/")
def health_check():
    return {
        "status": "running",
        "application": "Supplier Risk Platform"
    }


# -----------------------------
# Dashboard
# -----------------------------

@app.get("/dashboard")
def dashboard():

    # Replace with live aggregation later

    return {
        "total_suppliers": 0,
        "high_risk_suppliers": 0,
        "critical_suppliers": 0,
        "active_alerts": 0
    }


# -----------------------------
# Risk Trends
# -----------------------------

@app.get("/risk-trends")
def risk_trends():

    return {
        "data": []
    }


# -----------------------------
# Supplier Analysis
# -----------------------------

@app.post("/supplier-risk")
def supplier_risk(request: SupplierRequest):

    supplier_name = request.supplier

    # Financial Agent
    financial_data = financial_agent.analyze(
        supplier_name
    )

    # News Agent
    news_data = news_agent.analyze(
        supplier_name
    )

    # Compliance Agent
    compliance_data = compliance_agent.analyze(
        supplier_name
    )

    # Logistics Agent
    logistics_data = logistics_agent.analyze(
        supplier_name,
        request.country,
        request.location
    )

    # Social Media Agent
    socialmedia_data = social_agent.analyze(
        supplier_name
    )

    # Final Risk Score
    risk_result = risk_agent.calculate(
        financial_data,
        news_data,
        compliance_data,
        logistics_data,
        socialmedia_data
    )

    # Recommendations
    recommendations = recommendation_agent.generate(
        financial_data,
        news_data,
        compliance_data,
        logistics_data,
        socialmedia_data,
        risk_result["risk_score"]
    )

    # AI Summary
    summary = explanation_agent.generate_explanation(
        supplier_name=supplier_name,
        financial_data=financial_data,
        news_data=news_data,
        compliance_data=compliance_data,
        logistics_data=logistics_data,
        socialmedia_data=socialmedia_data,
        risk_score=risk_result["risk_score"],
        recommendations=recommendations
    )

    return {
        "supplier": supplier_name,
        "risk_score": risk_result["risk_score"],
        "risk_level": risk_result["risk_level"],
        "summary": summary,
        "financial_agent": financial_data,
        "news_agent": news_data,
        "compliance_agent": compliance_data,
        "logistics_agent": logistics_data,
        "socialmedia_agent": socialmedia_data,
        "recommendations": recommendations
    }


# -----------------------------
# Chat Endpoint
# -----------------------------

@app.post("/chat")
def chat(request: ChatRequest):

    response = explanation_agent.llm.invoke(
        request.query
    )

    return {
        "response": response.content
    }


# -----------------------------
# Run
# -----------------------------

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
