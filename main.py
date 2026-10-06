import argparse
from utils.spotify import get_track_info
from utils.updater import update_yt_dlp
from utils.youtube import download_song


def main(playlist_url):
    update_yt_dlp()
    print("Getting playlist details...")
    songs = get_track_info(playlist_url)
    print(f"Found {len(songs)} songs in the playlist.")
    print("Youtube download starting...")
    for index, s in enumerate(songs, start=1):
        title = s["title"]
        artist = s["artist"]
        download_song(title, artist, sequence=index)

    print("Download complete.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert Spotify playlist to YouTube downloads"
    )
    parser.add_argument(
        "--url", required=True, help="The Spotify playlist URL to convert"
    )
    args = parser.parse_args()
    main(args.url)
