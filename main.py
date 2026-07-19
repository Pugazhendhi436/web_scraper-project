from scraper import scrape_books
from save_data import save_csv
from database import save_database
from email_alert import send_email

from config import PRICE_LIMIT


def clean_price(price):

    return float(price.replace("Â£", ""))


def main():

    print("Scraping Website...")

    products = scrape_books()

    print(f"Books Found : {len(products)}")

    save_csv(products)

    save_database(products)

    for book in products:
        print(f"Checking Title  {book['Title']}")
        print(f"Price : {book['Price']}")
        print(f"Price Limit : £{PRICE_LIMIT}")
        print(f"Clean Price : £{clean_price(book['Price'])}")

        if clean_price(book["Price"]) < PRICE_LIMIT:

            print("Price Dropped")

            send_email(book)


if __name__ == "__main__":
    main()