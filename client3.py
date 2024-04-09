import time
import json
import urllib.request
import random

QUERY = "http://localhost:8080/query?id={}"

def getDataPoint(quote):
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2  # Compute the average price
    return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
    if price_b == 0:  # Handle division by zero
        return None  # Return None or handle the case as appropriate in your application
    return price_a / price_b

if __name__ == "__main__":
    N = 10  # Define the number of iterations
    prices = {}

    for _ in range(N):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price
            print("quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))
    
    print("Ratio %s" % getRatio(prices["ABC"], prices["DEF"]))
