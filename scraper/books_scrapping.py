import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

def books():

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    data = []

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").text

        rating = book.p["class"][1]

        availability = book.find_all("p")[1].text.strip()

        image = book.find("img")["src"]
        image = "https://books.toscrape.com/" + image.replace("../", "")

        data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "Image": image
        })

    return data