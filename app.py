
from flask import Flask
from flask import request
app = Flask(__name__)


@app.route("/")
def home():
    return "Try thihs route:"

@app.route('/login', methods=['GET'])
def login():
    if request.method == 'GET':
        tickerList = request.data
        rv = 
    else:
        return 

if __name__ == "__main__":
    app.run()