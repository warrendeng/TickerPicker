
from flask import Flask
from flask import request
app = Flask(__name__)

from stockTwitter import getSentiment

@app.route("/")
def home():
    return "Try this route:"

# @app.route('/queryList', methods=['GET'])
# def login():
#     if request.method == 'GET':
#         tickerList = request.data
#         rv = [getSentiment(s) for s in tickerList]
#         return rv
#     else:
#         return "bad"

@app.route('/query/<ticker>')
def login(ticker=None):
    return getSentiment(ticker)

if __name__ == "__main__":
    app.run()