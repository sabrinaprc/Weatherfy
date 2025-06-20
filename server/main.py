from fastapi import FastAPI
from routes.weather import router as weather_router
from fastapi.middleware.cors import CORSMiddleware
from routes.spotify_routes import router as spotify_router
from routes import gemini_routes
from routes import spotify_routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5050"],  # Vite's port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(spotify_routes.router)
app.include_router(spotify_router, prefix="/auth")
app.include_router(weather_router, prefix="/weather")
app.include_router(gemini_routes.router)
# app.include_router(gemini_routes.router, prefix="/ai")