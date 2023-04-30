from flask import Flask, render_template, request
#import MetaTrader5 as mt5
import config, json, requests

app = Flask(__name__)


@app.route('/')
def dashboard():
    return render_template('dashboard.html')


@app.route('/webhook', methods=['POST'])
def webhook():
    webhook_message = json.loads(request.data)

    price = webhook_message['strategy']['order_price']
    quantity = webhook_message['strategy']['order_contracts']
    symbol = webhook_message['ticker']
    side = webhook_message['strategy']['order_action']


if __name__ == '__main__':
    app.run(debug=True)


