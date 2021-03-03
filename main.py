from flask import Flask, render_template, url_for, redirect, send_file
from forms import TickerForm, CryptoForm
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import random

from util import *

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
        close_price = stock_history_df['Close'].tolist()
        # TODO date not working yet. faulty dataframe?
        # date = stock_history_df['Date'].tolist()

        stock_chart = create_plot(close_price)

        return render_template('home.html',
                                form=form, ticker=form.ticker.data,
                                is_ticker_found=is_ticker_found,
                                image_file=stock_chart,
                                tables=[stock_history_df.to_html(classes='data')], titles=stock_history_df.columns.values)

    return render_template('home.html', form=form, ticker=form.ticker.data)


# Page based on template
@app.route("/crypto", methods=['GET', 'POST'])
def crypto():
    form = CryptoForm()

    if form.validate_on_submit():
        # data = [1,3,5,7]
        # is_data_found = not(data.empty)
        is_data_found = True

        crpyto_chart = create_plot([3,1,5,1])

        return render_template('crypto.html',
                                form=form, crypto=form.crypto.data,
                                image_file=crpyto_chart,
                                is_data_found=is_data_found)

    return render_template('crypto.html', form=form, crypto=form.crypto.data)

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

if __name__ == '__main__':
    app.run(debug=True)
