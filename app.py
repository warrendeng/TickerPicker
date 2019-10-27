
from flask import Flask
from flask import request
from flask import json
app = Flask(__name__)

from stockTwitter import getSentiment

@app.route("/")
def home():
    return "Try querring at /singleSentiment/<ticker>!"

@app.route('/multiSentiment', methods=['GET'])
def queryList():
    if request.method == 'GET':
        tickerList = request.get_json()["data"]
        tickerListMap = [getSentiment(s) for s in tickerList]
        response = app.response_class(
          response=json.dumps(tickerListMap),
          status=200,
          mimetype='application/json'
        )
        return response
    else:
        return "bad"

@app.route('/sentiNN', methods=['GET'])
def queryList():
    if request.method == 'GET':
        tickerList = request.get_json()["data"]
        tickerListMap = [getSentiment(s) for s in tickerList]
        classificationMap = [danielMethod(s, tickerListMap[s]) for s in tickerListMap]
        response = app.response_class(
          response=json.dumps(tickerListMap),
          status=200,
          mimetype='application/json'
        )
        return response
    else:
        return "bad"

@app.route('/singleSentiment/<ticker>')
def querySingle(ticker=None):
    return getSentiment(ticker)

if __name__ == "__main__":
    app.run()