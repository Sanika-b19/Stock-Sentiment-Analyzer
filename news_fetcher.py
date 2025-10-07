import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")
NEWS_URL = "https://newsapi.org/v2/everything"

def fetch_news(query):
    params = {
        "q": query,
        "language": "en",
        "apiKey": API_KEY
    }
    response = requests.get(NEWS_URL, params=params)
    return response.json().get("articles", [])
