# Sandbox to do experiment
import yfinance as yf

def get_stock_info():
    msft = yf.Ticker("MSFT")
    #print(msft)

    history = msft.history(period="1mo", interval="1d") #return pandas dataframe
    #print(type(history))
    #print(history)
    return history

print("Hello world!")
df = get_stock_info()
print(df)
