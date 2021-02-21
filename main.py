from flask import Flask, render_template, url_for
import yfinance as yf
app = Flask(__name__)

def get_stock_info(ticker):
    ticker = yf.Ticker(ticker)
    history = ticker.history(period="1mo", interval="1d") #return pandas dataframe
    return history # return pandas DF

# Page based on template
@app.route("/")
def home():
    ticker = "MSFT"
    stock_history_df = get_stock_info(ticker)
    return render_template('home.html', ticker=ticker, tables=[stock_history_df.to_html(classes='data')], titles=stock_history_df.columns.values)

# Static page
@app.route("/about")
def about():
    return render_template('about.html')

# Static page
@app.route("/market")
def layout():
    return render_template('market.html')

if __name__ == '__main__':
    app.run(debug=True)
