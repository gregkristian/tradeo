from flask import Flask, render_template, url_for
import yfinance as yf
from forms import TickerForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'purupurupurupuru'

def get_stock_info(ticker):
    ticker = yf.Ticker(ticker)
    history = ticker.history(period="1mo", interval="1d") #return pandas dataframe
    return history # return pandas DF

# Page based on template
@app.route("/", methods=['GET', 'POST'])
def home():
    form = TickerForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('home.html', title='Register', form=form)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/market")
def market():
    ticker = "NDX"
    stock_history_df = get_stock_info(ticker)
    return render_template('market.html', ticker=ticker, tables=[stock_history_df.to_html(classes='data')], titles=stock_history_df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
