import requests
from bs4 import BeautifulSoup
from proxymanager import ProxyManager
import time

proxy_manager = ProxyManager('proxies.txt')
headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
}

def update():
    request = requests.get('https://mathewsteininger.com/sample-product', headers=headers,
                           proxies=proxy_manager.random_proxy())
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