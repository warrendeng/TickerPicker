from datetime import date
from gs_quant.data import Dataset
from gs_quant.markets.securities import SecurityMaster, AssetIdentifier
from gs_quant.session import GsSession
from twython import Twython 
import json
import sys
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
twitter = Twython('oGKKKOtLYiIOazQSKc1ciMu4q', 'fsZe6SGCi8CY6dK1vEniFK3eZr0z17KiL0ncLxBEx2aw2v4RGL')


client_id = '211a42c6a16244ccb1f9142ae9cc7fc1'
client_secret = '2f65f549b398ecbbe047933822dc0c2fa950f67158e9e6bbddc256ff5beaebf6'
scopes = GsSession.Scopes.get_default()
GsSession.use(client_id = client_id, client_secret = client_secret, scopes = scopes)
print("Enter a list of stock tickers separated by comma:")
stocks = input()
stockList = stocks.split(', ')
sentimentDict = {}
for stock in stockList:
	query = {'q': stock, 'result_type': 'popular', 'count': 100, 'lang': 'en'}
	sentimentScore = sentimentMagnitude = ctr = 0
	for status in twitter.search(**query)['statuses']:
		text = status['text']
		document = types.Document(
		    content=text,
		    type=enums.Document.Type.PLAIN_TEXT)

		# Detects the sentiment of the text
		sentiment = client.analyze_sentiment(document=document).document_sentiment
		sentimentScore += sentiment.score
		sentimentMagnitude += sentiment.magnitude
		ctr += 1
	sentimentDict[stock] = [sentimentScore / ctr, sentimentMagnitude / ctr]
print(sentimentDict)
		#print('Text: {}'.format(text))
		#print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))