from flask import Flask, render_template, url_for, redirect
import yfinance as yf
from forms import TickerForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'purupurupurupuru'

# Get stock info
# Return: panda dataframe containing price history. Empty dataframe if ticker not found
def get_stock_history(ticker):
    ticker = yf.Ticker(ticker)
    stock_history_df = ticker.history(period="1mo", interval="1d") #return pandas dataframe
    return stock_history_df # return pandas DF

# Page based on template
@app.route("/", methods=['GET', 'POST'])
def home():
    form = TickerForm() 
    app.logger.info('ticker data 1 %s', form.ticker.data)
    if form.validate_on_submit():
        app.logger.info('ticker data 2 %s', form.ticker.data)
        stock_history_df = get_stock_history(form.ticker.data)
        is_ticker_found = not(stock_history_df.empty)

        return render_template('home.html',
                                form=form, ticker=form.ticker.data,
                                is_ticker_found=is_ticker_found,
                                tables=[stock_history_df.to_html(classes='data')], titles=stock_history_df.columns.values)                    

    return render_template('home.html', form=form, ticker=form.ticker.data)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/market")
def market():
    ticker = "NDX"
    stock_history_df = get_stock_history(ticker)
    return render_template('market.html', 
                            ticker=ticker,
                            tables=[stock_history_df.to_html(classes='data')], titles=stock_history_df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
