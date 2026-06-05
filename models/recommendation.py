# models/recommendation.py
# Recommendation Model

from typing import List, Optional
from pydantic import BaseModel, Field


class Recommendation(BaseModel):
    title: str = Field(
        ...,
        description="Recommendation title"
    )

    description: str = Field(
        ...,
        description="Detailed recommendation"
    )

    priority: str = Field(
        ...,
        description="LOW | MEDIUM | HIGH | CRITICAL"
    )

    category: str = Field(
        ...,
        description="Financial, Compliance, Logistics, Social Media, News"
    )


class RecommendationResponse(BaseModel):
    supplier: str

    risk_score: float

    risk_level: str

    recommendations: List[Recommendation]

    generated_by: Optional[str] = "RecommendationAgent"
