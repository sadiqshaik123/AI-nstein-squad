# api/routes.py

from fastapi import APIRouter

from api.schemas import (
    SupplierRequest,
    SupplierRiskResponse,
    ChatRequest,
    ChatResponse,
    DashboardResponse,
    RiskTrendResponse
)

from agents.financial_agent import FinancialAgent
from agents.news_agent import NewsAgent
from agents.compliance_agent import ComplianceAgent
from agents.logistics_agent import LogisticsAgent
from agents.socialmedia import SocialMediaAgent
from agents.risk_scoring_agent import RiskScoringAgent
from agents.recommendation_agent import RecommendationAgent
from agents.explanation_agent import ExplanationAgent

router = APIRouter()

# -----------------------------------
# Initialize Agents
# -----------------------------------

financial_agent = FinancialAgent()
news_agent = NewsAgent()
compliance_agent = ComplianceAgent()
logistics_agent = LogisticsAgent()
socialmedia_agent = SocialMediaAgent()

risk_agent = RiskScoringAgent()
recommendation_agent = RecommendationAgent()
explanation_agent = ExplanationAgent()

# -----------------------------------
# Dashboard
# -----------------------------------

@router.get(
    "/dashboard",
    response_model=DashboardResponse
)
def dashboard():

    return {
        "total_suppliers": 0,
        "high_risk_suppliers": 0,
        "critical_suppliers": 0,
        "active_alerts": 0
    }


# -----------------------------------
# Risk Trends
# -----------------------------------

@router.get(
    "/risk-trends",
    response_model=RiskTrendResponse
)
def risk_trends():

    return {
        "data": []
    }


# -----------------------------------
# Supplier Risk Analysis
# -----------------------------------

@router.post(
    "/supplier-risk",
    response_model=SupplierRiskResponse
)
def supplier_risk(
    request: SupplierRequest
):

    supplier_name = request.supplier

    financial_data = financial_agent.analyze(
        supplier_name
    )

    news_data = news_agent.analyze(
        supplier_name
    )

    compliance_data = compliance_agent.analyze(
        supplier_name
    )

    logistics_data = logistics_agent.analyze(
        supplier_name,
        request.country,
        request.location
    )

    socialmedia_data = socialmedia_agent.analyze(
        supplier_name
    )

    risk_result = risk_agent.calculate(
        financial_data,
        news_data,
        compliance_data,
        logistics_data,
        socialmedia_data
    )

    recommendations = recommendation_agent.generate(
        financial_data,
        news_data,
        compliance_data,
        logistics_data,
        socialmedia_data,
        risk_result["risk_score"]
    )

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


# -----------------------------------
# Chat Endpoint
# -----------------------------------

@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(
    request: ChatRequest
):

    response = explanation_agent.llm.invoke(
        request.query
    )

    return {
        "response": response.content
    }
