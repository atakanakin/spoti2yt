import os
import re
import subprocess

OUT_DIR = "audio"
os.makedirs(OUT_DIR, exist_ok=True)


def slugify(text: str) -> str:
    tr_map = {
        "ç": "c",
        "Ç": "c",
        "ğ": "g",
        "Ğ": "g",
        "ı": "i",
        "İ": "i",
        "ö": "o",
        "Ö": "o",
        "ş": "s",
        "Ş": "s",
        "ü": "u",
        "Ü": "u",
    }
    for k, v in tr_map.items():
        text = text.replace(k, v)

    text = text.lower()

    # FAT32 illegal chars: \ / : * ? " < > |
    text = re.sub(r'[\\/:*?"<>|]', "", text)
    text = re.sub(r"[^a-z0-9\- _]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:120]


def download_song(title: str, artist: str):
    safe_title = slugify(title)
    safe_artist = slugify(artist)

    out_name = f"{safe_title} - {safe_artist}.mp3"
    out_path = os.path.join(OUT_DIR, out_name)

    query = f"{title} - {artist}"

    cmd = [
        "yt-dlp",
        f"ytsearch1:{query}",
        "-x",
        "--audio-format",
        "mp3",
        "--audio-quality",
        "128K",
        "--postprocessor-args",
        "ffmpeg:-ar 44100 -ac 2 -acodec libmp3lame",
        "-o",
        out_path,
    ]

    subprocess.run(cmd, check=False, shell=True)
