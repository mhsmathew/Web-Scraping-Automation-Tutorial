import requests
from bs4 import BeautifulSoup
import time


def update():
    request = requests.get('https://mathewsteininger.com/sample-product')
    html = request.content
    soup = BeautifulSoup(html, 'html.parser')
    # Monitor this tag to check stock changes
    stock = soup.find("button", {"id": "availability"})
    # Monitor this tag to check price changes
    price = soup.find("div", {"id": "price"})
    return stock, price


stock, price = update()
while True:
    time.sleep(2)
    updated_stock, updated_price = update()
    if (stock, price) != (updated_stock, updated_price):
        # Could connect notification API here
        print("Price or Stock Changed!")
        stock, price = updated_stock, updated_price
    else:
        print("No Update")


