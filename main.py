from pickle import TRUE
from time import sleep
from bs4 import BeautifulSoup as bs
from numpy import double
import requests
import re

old_price = 0

while TRUE:
    page = requests.get("https://www.google.com/finance/quote/EUR-RUB")
    soup = bs(page.content, features="html.parser")
    price = soup.find(class_="YMlKec fxKbKc").string
    shit = re.sub('[^a-zA-Z]+', "", price)

    if (double(price) > old_price):
        old_price = double(price)

    # (Euro to Ruble)
    print("\nCurrent Ruble price: ", price)
    print("Highest price recorded by me: ", old_price)
    sleep(60)
