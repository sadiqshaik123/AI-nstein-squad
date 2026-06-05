# api/schemas.py
# Pydantic Request/Response Models

from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


# -----------------------------
# Requests
# -----------------------------

class SupplierRequest(BaseModel):
    supplier: str = Field(
        ...,
        description="Supplier Name"
    )

    country: Optional[str] = None
    location: Optional[str] = None


class ChatRequest(BaseModel):
    query: str


# -----------------------------
# Agent Responses
# -----------------------------

class FinancialResponse(BaseModel):
    financial_score: float
    risk_level: str


class NewsResponse(BaseModel):
    news_score: float
    risk_level: str


class ComplianceResponse(BaseModel):
    compliance_score: float
    risk_level: str


class LogisticsResponse(BaseModel):
    overall_logistics_score: float
    risk_level: str


class SocialMediaResponse(BaseModel):
    social_score: float
    risk_level: str


# -----------------------------
# Supplier Risk Response
# -----------------------------

class SupplierRiskResponse(BaseModel):

    supplier: str

    risk_score: float

    risk_level: str

    summary: str

    financial_agent: Dict[str, Any]

    news_agent: Dict[str, Any]

    compliance_agent: Dict[str, Any]

    logistics_agent: Dict[str, Any]

    socialmedia_agent: Dict[str, Any]

    recommendations: List[str]


# -----------------------------
# Dashboard Response
# -----------------------------

class DashboardResponse(BaseModel):

    total_suppliers: int

    high_risk_suppliers: int

    critical_suppliers: int

    active_alerts: int


# -----------------------------
# Risk Trend Response
# -----------------------------

class RiskTrendPoint(BaseModel):

    date: str

    risk_score: float


class RiskTrendResponse(BaseModel):

    data: List[RiskTrendPoint]


# -----------------------------
# Chat Response
# -----------------------------

class ChatResponse(BaseModel):

    response: str
