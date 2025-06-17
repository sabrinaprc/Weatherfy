from fastapi import APIRouter, Query
from services.weather_api import get_weather_by_location

router = APIRouter()

@router.get("/")
async def get_weather(lat: float = Query(...), lon: float = Query(...)):
    return await get_weather_by_location(lat, lon)