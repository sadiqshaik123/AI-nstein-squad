# models/risk.py
# Risk Models

from typing import Dict, Optional
from pydantic import BaseModel, Field


class RiskBreakdown(BaseModel):
    financial_score: float = Field(default=0)
    news_score: float = Field(default=0)
    compliance_score: float = Field(default=0)
    logistics_score: float = Field(default=0)
    social_score: float = Field(default=0)


class RiskScore(BaseModel):
    supplier: str

    risk_score: float = Field(
        ...,
        description="Overall risk score"
    )

    risk_level: str = Field(
        ...,
        description="LOW | MEDIUM | HIGH | CRITICAL"
    )

    score_breakdown: RiskBreakdown

    generated_by: Optional[str] = "RiskScoringAgent"


class SupplierRiskProfile(BaseModel):
    supplier: str

    financial_data: Dict

    news_data: Dict

    compliance_data: Dict

    logistics_data: Dict

    socialmedia_data: Dict

    risk_score: RiskScore
