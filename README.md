# spoti2yt

A tool to convert Spotify playlists to YouTube audio downloads.

## Installation

1. Install `uv`:

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Clone or download this repository.

3. Install dependencies:
   ```bash
   uv sync
   ```

## Usage

Run the script with a Spotify playlist URL:

```bash
uv run main.py --playlist-url "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID"
```

This will scrape the playlist and download each song as MP3 to the `audio/` directory.

## Environment Variables

1. Create a Spotify app at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).

2. Copy `example.env` to `.env`:

   ```bash
   cp example.env .env
   ```

3. Edit `.env` with your credentials:

   ```
   SPOTIPY_CLIENT_ID=your_client_id
   SPOTIPY_CLIENT_SECRET=your_client_secret
   ```

## Requirements

- Python 3.14+
- yt-dlp (installed via dependencies)
- Spotify developer account
