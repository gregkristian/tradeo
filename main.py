from os import environ, path
from dotenv import load_dotenv
from flask import Flask, render_template, url_for, redirect, send_file
from forms import TickerForm, CryptoForm
import sys

from util import *
# from api_client import *

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

app = Flask(__name__)

if "SECRET_KEY" not in environ:
    print('Error: Flask SECRET_KEY not set. Exiting')
    sys.exit(1)

app.config['SECRET_KEY'] = environ.get('SECRET_KEY')

# Page based on template
@app.route("/", methods=['GET', 'POST'])
def home():
    form = TickerForm()
    if form.validate_on_submit():
        stock_history_df = get_stock_history(form.ticker.data)

        if not(stock_history_df.empty):
            close_prices = stock_history_df['Close'].tolist()
            # Get df index (date) with type pd Timestamp and convert to py Datetime
            dates_index = stock_history_df.index.tolist()
            dates = list(map(lambda x: x.to_pydatetime(), dates_index))

        return render_template('home.html',
                                form=form, ticker=form.ticker.data,
                                is_ticker_found=is_ticker_found,
                                close_prices=close_prices,
                                dates=dates,
                                tables=[stock_history_df.to_html(classes='data')], titles=stock_history_df.columns.values)

    return render_template('home.html', form=form, ticker=form.ticker.data)


# Page based on template
""" @app.route("/crypto", methods=['GET', 'POST'])
def crypto():
    form = CryptoForm()

    if form.validate_on_submit():
        is_data_found = True

        client = get_client()

        klines = client.get_historical_klines(form.crypto.data,
                                              client.KLINE_INTERVAL_30MINUTE, "1 day ago UTC")

        close_price = [int(float(el[4])) for el in klines]

        return render_template('crypto.html',
                                form=form, crypto=form.crypto.data,
                                is_data_found=is_data_found)

    return render_template('crypto.html', form=form, crypto=form.crypto.data) """

# Static about page
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

# Dev for sandbox
@app.route("/dev")
def dev():
    return render_template('dev.html',
                            img1=url_for('static', filename = 'img1.png'),
                            img2=url_for('static', filename = 'img2.png'),
                            img3=url_for('static', filename = 'img3.png'))

if __name__ == '__main__':
    app.run(debug=True)
