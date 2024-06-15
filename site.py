from flask import Flask, render_template
import requests

app = Flask(__name__)

API_URL = 'https://api.exchangerate-api.com/v4/latest/USD'

@app.route("/")
def start_menu():
    return render_template("start-menu.html")

@app.route("/exchange_rate")
def exchange_rate():
    return render_template("exchange rate.html")

@app.route('/exchange_rate_start')
def index():
    response = requests.get(API_URL)
    data = response.json()

    # Курсы валют относительно рубля
    rates = data['rates']
    currencies = {
        'Доллар': 1 / rates['USD'],
        'Евро': 1 / rates['EUR'],
        'Юань': 1 / rates['CNY']
    }

    return render_template('exchange_rate_start.html', currencies=currencies)

if __name__ == "__main__":
    app.run()