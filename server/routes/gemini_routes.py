# server/routes/gemini_routes.py
from fastapi import APIRouter, Query
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
router = APIRouter()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@router.get("/mood-genres")
def get_seed_genres(
    weather_description: str = Query(...),
):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
            Choose 3 to 5 seed genres from the Spotify genre list that match the mood of the weather: '{weather_description}'.

            Only respond with a Python list of strings like:
            ["chill", "acoustic", "pop"]
            """,
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_budget=0)
            )
        )

        print("🔁 Gemini raw response:", response.text)
        genres = eval(response.text.strip())
        return {"genres": genres}

    except Exception as e:
        print("❌ ERROR:", str(e))
        return {"error": "Internal Server Error", "details": str(e)}