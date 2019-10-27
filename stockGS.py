from datetime import date
from gs_quant.session import GsSession

import requests
import json

import pandas as pd

client_id="211a42c6a16244ccb1f9142ae9cc7fc1"
client_secret="2f65f549b398ecbbe047933822dc0c2fa950f67158e9e6bbddc256ff5beaebf6"

# enter marquee
scopes = GsSession.Scopes.get_default()
GsSession.use(client_id=client_id, client_secret=client_secret, scopes=scopes)

session = requests.Session()

auth_data = {
    'grant_type'    : 'client_credentials',
    'client_id'     : client_id,
    'client_secret' : client_secret,
    'scope'         : 'read_product_data'
}
auth_request = session.post("https://idfs.gs.com/as/token.oauth2", data = auth_data)
access_token_dict = json.loads(auth_request.text)
access_token = access_token_dict["access_token"]

# update session headers with access token
session.headers.update({"Authorization":"Bearer "+ access_token})
# api-endpoint 
URL = "https://api.marquee.gs.com/v1/assets/data/query"
  
# defining a params dict for the parameters to be sent to the API 
headers = {
    'Content-Type': 'application/json'
}

def getInfo(tickerList):
	jsonInput = {
	    "where": {
	        "ticker": tickerList,
	#         "listed": True,
	#         "assetClassificationsIsPrimary": True,
	        "currency": "USD",
	        "assetClass": "Equity"
	    },
	    "fields": [ "ticker", "gsid", "name"],
	    "limit": len(tickerList)
	}
	  
	# sending get request and saving the response as response object 
	r = session.post(URL, headers=headers, json=jsonInput) 
	  
	# extracting data in json format 
	tickerMap = {}
	ctr = 0
	for d in r.json()["results"]:
		ctr += 1
		name, gsid, ticker = d["name"], d["gsid"], d["ticker"]
		print(name, gsid, ticker, sep=' @ ')
		print(ctr)
		tickerMap[ticker] = {"name": name, "gsid": gsid}
		# break
	return tickerMap