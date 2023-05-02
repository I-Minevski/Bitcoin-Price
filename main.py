import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.binance.com/en/price/bitcoin'
req = requests.get(url)

soup = bs(req.content, 'html.parser')

price = soup.find('div', class_='css-12ujz79')

print(f"The Bitcoin price now is {price.text} per (BTC/USD)")