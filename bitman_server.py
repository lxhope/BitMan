#!/usr/bin/env python3
# -*- coding: utf8 -*-

from flask import Flask
from flask import request

from HuobiServices import get_current_price


app = Flask(__name__)

@app.route("/")
def price():
    symbol = request.args.get('symbol', 'btc')
    symbol = symbol + 'usdt'
    price = get_current_price(symbol)
    return str(price)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)