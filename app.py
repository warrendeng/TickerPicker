
from flask import Flask
from flask import request
from flask import json
app = Flask(__name__)

from stockTwitter import getSentiment

@app.route("/")
def home():
    return "Try querring at /query/<ticker>!"

@app.route('/queryList', methods=['GET'])
def queryList():
    if request.method == 'GET':
        tickerList = request.get_json()
        tickerListMap = [getSentiment(s) for s in tickerList]
        response = app.response_class(
          response=json.dumps(tickerListMap),
          status=200,
          mimetype='application/json'
        )
        return response
    else:
        return "bad"

@app.route('/query/<ticker>')
def querySingle(ticker=None):
    return getSentiment(ticker)

if __name__ == "__main__":
    app.run()