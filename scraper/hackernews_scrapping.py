import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/?p=2"

def hackernews():

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    data = []

    news = soup.find_all("span", class_="titleline")

    for item in news:

        a_tag = item.find("a")

        title = a_tag.get_text(strip=True) if a_tag else "N/A"
        link = a_tag.get("href") if a_tag else "N/A"

        data.append({
            "Title": title,
            "Link": link
        })

    return data