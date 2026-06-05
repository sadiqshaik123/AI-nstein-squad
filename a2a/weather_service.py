from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import random

app = FastAPI(
    title="A2A Weather Risk Service",
    version="1.0.0"
)


class WeatherRequest(BaseModel):
    supplier: str
    country: str | None = None
    location: str | None = None


@app.get("/")
def health_check():
    return {
        "status": "running",
        "service": "weather-risk-agent",
        "timestamp": datetime.utcnow().isoformat()
    }


@app.post("/weather-risk")
def weather_risk(request: WeatherRequest):

    # POC Logic
    # Replace later with:
    # - OpenWeather API
    # - WeatherAPI
    # - NOAA
    # - AccuWeather

    storm_risk = random.randint(0, 100)
    flood_risk = random.randint(0, 100)
    temperature_risk = random.randint(0, 100)

    weather_score = round(
        (
            storm_risk * 0.4 +
            flood_risk * 0.35 +
            temperature_risk * 0.25
        ),
        2
    )

    if weather_score >= 75:
        risk_level = "HIGH"
    elif weather_score >= 50:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return {
        "supplier": request.supplier,
        "location": request.location,
        "country": request.country,
        "weather_score": weather_score,
        "risk_level": risk_level,
        "storm_risk": storm_risk,
        "flood_risk": flood_risk,
        "temperature_risk": temperature_risk,
        "recommendation": (
            "Monitor weather disruptions and increase inventory buffer"
            if weather_score >= 75
            else "Continue weather monitoring"
        )
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=9002
    )
