# spoti2yt

Download a Spotify playlist as MP3 files by searching each track on YouTube.
Dependencies and the Python environment are managed with [uv](https://docs.astral.sh/uv/).

On every run the tool first upgrades `yt-dlp` to the latest release, so
downloads don't break when YouTube changes something.

## Setup

### 1. Spotify credentials

1. Create an app in the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).
2. Copy `example.env` to `.env` and fill it in:

   ```bash
   cp example.env .env
   ```

   ```
   SPOTIPY_CLIENT_ID="your_client_id"
   SPOTIPY_CLIENT_SECRET="your_client_secret"
   ```

### 2. Install on desktop (macOS / Linux)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
git clone <repo-url> spoti2yt && cd spoti2yt
uv sync
```

### 3. Install on Android (Termux)

```bash
pkg update && pkg upgrade
pkg install git uv ffmpeg
termux-setup-storage          # grants access to ~/storage/downloads

git clone <repo-url> ~/spoti2yt && cd ~/spoti2yt
cp example.env .env           # then edit .env with your credentials
uv sync
```

Files are saved to `~/storage/downloads/spoti2yt` (see `OUT_DIR` in
`utils/youtube.py`). Existing `.mp3` files in that folder are deleted at the
start of each run.

#### Shell function (Termux)

Add a small function to `~/.bashrc` (or `~/.zshrc` if you use zsh) so a single
command does everything:

```bash
s() {
    if [ -z "$1" ]; then
        echo "Error: no link given. Usage: s <spotify-link>"
        return 1
    fi
    (cd ~/spoti2yt && uv run main.py --url "$1")
}
```

Reload your shell config:

```bash
source ~/.bashrc
```

Now paste a link in Termux:

```bash
s "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID"
```

## Usage

```bash
uv run main.py --url "https://open.spotify.com/playlist/YOUR_PLAYLIST_ID"
```

Each song is downloaded as `NN title - artist.mp3`, where `NN` is its position
in the playlist.

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- [ffmpeg](https://ffmpeg.org/) (for audio extraction)
