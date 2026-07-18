import requests
from bs4 import BeautifulSoup


def spotify():

    url = "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    songs_data = []

    # Song titles
    titles = soup.find_all("meta", attrs={"name": "music:song"})

    for i, title in enumerate(titles, start=1):
        songs_data.append({
            "No": i,
            "Song": title.get("content"),
        })

    return songs_data