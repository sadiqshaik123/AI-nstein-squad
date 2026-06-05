from fastapi import FastAPI
from pydantic import BaseModel
import random
from datetime import datetime

app = FastAPI(
    title="A2A Logistics Risk Service",
    version="1.0.0"
)


class SupplierRequest(BaseModel):
    supplier: str
    country: str | None = None


@app.get("/")
def health():
    return {
        "status": "running",
        "service": "logistics-risk-agent",
        "timestamp": datetime.utcnow().isoformat()
    }


@app.post("/logistics-risk")
def logistics_risk(request: SupplierRequest):

    # Replace these mocked values later with:
    # - Weather API
    # - MarineTraffic API
    # - Shipping API
    # - Port Congestion API

    port_congestion_score = random.randint(20, 90)
    weather_risk_score = random.randint(10, 80)
    transportation_delay_score = random.randint(20, 90)

    logistics_score = round(
        (
            port_congestion_score * 0.4 +
            weather_risk_score * 0.3 +
            transportation_delay_score * 0.3
        ),
        2
    )

    if logistics_score >= 75:
        risk_level = "HIGH"
    elif logistics_score >= 50:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return {
        "supplier": request.supplier,
        "risk_level": risk_level,
        "logistics_score": logistics_score,
        "port_congestion_score": port_congestion_score,
        "weather_risk_score": weather_risk_score,
        "transportation_delay_score": transportation_delay_score,
        "recommendation": (
            "Increase safety stock and monitor shipment routes"
            if logistics_score >= 75
            else "Continue monitoring logistics indicators"
        )
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=9001
    )
