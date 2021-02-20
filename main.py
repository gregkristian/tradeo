from flask import Flask, render_template, url_for
import yfinance as yf
app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

# Page based on template
@app.route("/")
def home():
    return render_template('index.html', posts=posts)

# Static page
@app.route("/about")
def about():
    return "<h1>About Page</h1>"

if __name__ == '__main__':
    app.run(debug=True)

def stock():
    msft = yf.Ticker("MSFT")
    print(msft)

    history = msft.history(period="1mo", interval="1d") #return pandas dataframe
    print(type(history))
    print(history)
