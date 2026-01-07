import requests
from bs4 import BeautifulSoup


def get_track_info(playlist_url: str, debug: bool = False):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9",
    }

    r = requests.get(playlist_url, headers=headers)
    r.raise_for_status()

    if debug:
        with open("test.html", "w", encoding="utf-8") as f:
            f.write(r.text)

    soup = BeautifulSoup(r.text, "html.parser")

    songs = []

    for row in soup.select('[data-testid="track-row"]'):
        title_el = row.select_one('p[data-encore-id="listRowTitle"] span')
        artist_el = row.select_one("div.p84CwlsfChh7dMblxPTU span")

        if not title_el or not artist_el:
            continue

        title = title_el.get_text(strip=True)
        artist = artist_el.get_text(strip=True)

        songs.append(
            {
                "title": title,
                "artist": artist,
            }
        )

    print(f"{len(songs)} songs found\n")
    for s in songs:
        print(f'{s["artist"]} - {s["title"]}')

    return songs
