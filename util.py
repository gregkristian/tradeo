from io import BytesIO
from matplotlib.figure import Figure
from flask import url_for
import yfinance as yf

# Get stock info
# Return: panda dataframe containing price history. Empty dataframe if ticker not found
def get_stock_history(aTicker):
    ticker = yf.Ticker(aTicker)
    stock_history_df = ticker.history(period="1mo", interval="1d")
    return stock_history_df
