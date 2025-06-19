from fastapi import FastAPI
from routes.weather import router as weather_router
from fastapi.middleware.cors import CORSMiddleware
from routes.spotify_routes import router as spotify_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5050"],  # Vite's port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(weather_router, prefix="/weather")
app.include_router(spotify_router, prefix="/auth")