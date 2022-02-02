from flask import Flask, render_template, url_for, redirect, send_file
from forms import TickerForm, CryptoForm
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import random
import sys

from util import *
# from api_client import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'purupurupurupuru'


# Page based on template
@app.route("/", methods=['GET', 'POST'])
def home():
    form = TickerForm()
    if form.validate_on_submit():
        stock_history_df = get_stock_history(form.ticker.data)

        is_ticker_found = not(stock_history_df.empty)

        stock_history_df = get_stock_history(form.ticker.data)
        close_prices = stock_history_df['Close'].tolist()

        # Get df index (date) with type pd Timestamp and convert to py Datetime
        dates_index = stock_history_df.index.tolist()
        dates = list(map(lambda x: x.to_pydatetime(), dates_index))

        stock_chart = create_plot(close_prices)

        return render_template('home.html',
                                form=form, ticker=form.ticker.data,
                                is_ticker_found=is_ticker_found,
                                close_prices=close_prices,
                                dates=dates,
                                image_file=stock_chart,
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

        crpyto_chart = create_plot(close_price)

        return render_template('crypto.html',
                                form=form, crypto=form.crypto.data,
                                image_file=crpyto_chart,
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
