import os
import requests
from dotenv import load_dotenv


def get_auth_token():
    """Get Spotify API auth token using Client Credentials Flow"""
    load_dotenv()
    url = "https://accounts.spotify.com/api/token"

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    data = {
        "grant_type": "client_credentials",
        "client_id": os.getenv("SPOTIPY_CLIENT_ID"),
        "client_secret": os.getenv("SPOTIPY_CLIENT_SECRET"),
    }

    r = requests.post(url, headers=headers, data=data)

    if r.status_code != 200:
        raise RuntimeError(f"Failed to get token {r.status_code} - {r.text}")

    return r.json()["access_token"]


def get_track_info(playlist_url: str) -> list[dict]:
    token = get_auth_token()
    """Fetch multiple pages of tracks from the API"""
    # Extract Playlist ID from URL
    if "playlist/" in playlist_url:
        playlist_id = playlist_url.split("playlist/")[1].split("?")[0]
    else:
        playlist_id = playlist_url

    api_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

    headers = {"Authorization": f"Bearer {token}"}

    songs = []
    while api_url:
        r = requests.get(api_url, headers=headers)

        if r.status_code != 200:
            print(f"Error: {r.status_code} - {r.text}")
            break

        data = r.json()
        items = data.get("items", [])

        for item in items:
            track = item.get("track")
            # Check for local files or corrupted data
            if not track or track.get("is_local"):
                continue

            name = track["name"]
            artist = track["artists"][0]["name"] if track["artists"] else ""
            songs.append({"title": name, "artist": artist})

        # Handle pagination
        api_url = data.get("next")
        if api_url:
            print(f"{len(songs)} songs found, continuing...")

    return songs
