import requests
from bs4 import BeautifulSoup

from config import URL


def scrape_books():

    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    products = []

    for book in books:

        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").text

        rating = book.p["class"][1]

        availability = book.find(
            "p",
            class_="instock availability"
        ).text.strip()

        products.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability
        })

    return products