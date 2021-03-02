from matplotlib.figure import Figure
import yfinance as yf

# Get stock info
# Return: panda dataframe containing price history. Empty dataframe if ticker not found
def get_stock_history(ticker):
    ticker = yf.Ticker(ticker)
    stock_history_df = ticker.history(period="1mo", interval="1d")
    return stock_history_df

# Create a plot from 1 dimensional data
def create_plot(data):
    fig = Figure()
    subplot = fig.subplots()
    subplot.plot(data)
    return fig
