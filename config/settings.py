from dotenv import load_dotenv
import os

load_dotenv()

GENAI_BASE_URL = os.getenv("GENAI_BASE_URL")
GENAI_API_KEY = os.getenv("GENAI_API_KEY")

LLM_MODEL = os.getenv("LLM_MODEL")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

MCP_SERVER_URL = os.getenv("MCP_SERVER_URL")

LOGISTICS_SERVICE_URL = os.getenv("LOGISTICS_SERVICE_URL")
WEATHER_SERVICE_URL = os.getenv("WEATHER_SERVICE_URL")

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")

KAGGLE_USERNAME = os.getenv("KAGGLE_USERNAME")
KAGGLE_KEY = os.getenv("KAGGLE_KEY")