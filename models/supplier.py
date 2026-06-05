# models/supplier.py
# Supplier Models

from typing import Optional, List
from pydantic import BaseModel, Field


class Supplier(BaseModel):
    supplier_name: str = Field(
        ...,
        description="Supplier name"
    )

    country: Optional[str] = None

    location: Optional[str] = None

    category: Optional[str] = None

    industry: Optional[str] = None

    contact_email: Optional[str] = None

    website: Optional[str] = None


class SupplierFinancialProfile(BaseModel):
    credit_score: Optional[float] = None

    debt_ratio: Optional[float] = None

    revenue_growth: Optional[float] = None

    financial_score: Optional[float] = None


class SupplierComplianceProfile(BaseModel):
    compliance_score: Optional[float] = None

    violations: Optional[int] = 0

    esg_rating: Optional[str] = None

    iso_certified: Optional[bool] = False


class SupplierLogisticsProfile(BaseModel):
    logistics_score: Optional[float] = None

    weather_score: Optional[float] = None

    port_congestion_score: Optional[float] = None


class SupplierSocialProfile(BaseModel):
    social_score: Optional[float] = None

    positive_mentions: Optional[int] = 0

    negative_mentions: Optional[int] = 0


class SupplierProfile(BaseModel):
    supplier: Supplier

    financial_profile: Optional[
        SupplierFinancialProfile
    ] = None

    compliance_profile: Optional[
        SupplierComplianceProfile
    ] = None

    logistics_profile: Optional[
        SupplierLogisticsProfile
    ] = None

    social_profile: Optional[
        SupplierSocialProfile
    ] = None

    tags: List[str] = []


class SupplierSummary(BaseModel):
    supplier_name: str

    risk_score: float

    risk_level: str

    recommendation_count: int

    summary: str
