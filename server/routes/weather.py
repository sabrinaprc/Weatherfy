from fastapi import APIRouter, Query
from services.weather_api import get_weather_by_location

router = APIRouter()

@router.get("/")
async def get_weather(city: str = Query(None), lat: float = Query(None), lon: float = Query(None)):
    return await get_weather_by_location(city, lat, lon)
