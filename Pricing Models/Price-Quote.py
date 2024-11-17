#Yahoo Finance API
from .Black_Scholes import blackScholesEquation
import yfinance as yf

ticker = yf.Ticker("AAPL")

opt_chain = ticker.option_chain()

print(opt_chain.calls)