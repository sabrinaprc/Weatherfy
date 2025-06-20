from spotify_routes import get_spotify_seed_genres

CLIENT_ID = "your_actual_client_id"
CLIENT_SECRET = "your_actual_client_secret"

genres = get_spotify_seed_genres(CLIENT_ID, CLIENT_SECRET)
print(genres)