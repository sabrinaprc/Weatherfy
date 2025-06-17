import os
import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

async def get_weather_by_location(city=None, lat=None, lon=None):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "appid": API_KEY,
        "units": "metric"
    }

    if city:
        params["q"] = city
    elif lat and lon:
        params["lat"] = lat
        params["lon"] = lon
    else:
        return {"error": "Missing city or coordinates"}

    async with httpx.AsyncClient() as client:
        response = await client.get(base_url, params=params)
        data = response.json()
        return {
            "location": data.get("name"),
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["main"],
            "icon": data["weather"][0]["icon"]
        }
