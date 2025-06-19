# libs/llama_client.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL")
OLLAMA_ENDPOINT = f"{OLLAMA_URL}/api/generate"

def get_ai_category_recommendation(description, category_names):
    prompt = (
        "Given the following list of categories:\n"
        f"{', '.join(category_names)}\n\n"
        f"Which category best fits the following activity:\n"
        f"\"{description}\"\n\n"
        "Respond with only the category name from the list. If nothing fits, choose the closest."
    )

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload)
        result = response.json()
        return result.get("response", "").strip()
    except Exception as e:
        print("❌ LLaMA3 AI call failed:", e)
        return None
