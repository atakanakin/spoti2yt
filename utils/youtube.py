import glob
import os
import re
import subprocess

# for termux use /storage/emulated/0/storage/downloads/spoti2yt
OUT_DIR = os.path.join(os.path.expanduser("~"), "storage", "downloads", "spoti2yt")
os.makedirs(OUT_DIR, exist_ok=True)
mp3_files = glob.glob(os.path.join(OUT_DIR, "*.mp3"))

if not mp3_files:
    pass

for f in mp3_files:
    try:
        os.remove(f)
    except OSError as e:
        pass


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
    print(f"Downloading: {title} - {artist}")
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

    subprocess.run(cmd, check=False)
