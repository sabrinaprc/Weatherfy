# server/routes/spotify_routes.py
from fastapi import APIRouter, Request
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

sp_oauth = SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="user-top-read user-read-private"
)

@router.get("/login")
def login():
    auth_url = sp_oauth.get_authorize_url()
    return {"auth_url": auth_url}

@router.get("/callback")
def callback(request: Request):
    code = request.query_params.get("code")
    token_info = sp_oauth.get_access_token(code, check_cache=False)
    return {"access_token": token_info["access_token"]}

@router.get("/me")
def get_user_profile():
    token_info = sp_oauth.get_cached_token()
    if not token_info:
        return {"error": "No token found. Please log in first."}
    
    access_token = token_info["access_token"]
    sp = spotipy.Spotify(auth=access_token)
    profile = sp.current_user()
    return profile