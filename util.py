from io import BytesIO
from matplotlib.figure import Figure
from flask import url_for
import yfinance as yf

# Get stock info
# Return: panda dataframe containing price history. Empty dataframe if ticker not found
def get_stock_history(ticker):
    ticker = yf.Ticker(ticker)
    stock_history_df = ticker.history(period="1mo", interval="1d")
    return stock_history_df

# Create a plot from 1 dimensional list, return image url
# TODO accept panda dataframe instead
def create_plot(data):
    print(data)
    fig = Figure()
    subplot = fig.subplots()
    subplot.plot(data)

    img = BytesIO()
    fig.savefig('static/image.png', format="png", dpi=200)
    # TODO avoid cache
    img.seek(0)
    image_url = url_for('static', filename = 'image.png')

    return image_url
