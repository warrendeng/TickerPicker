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
from stockGS import getInfo

client = language.LanguageServiceClient()

# The text to analyze
twitter = Twython('oGKKKOtLYiIOazQSKc1ciMu4q', 'fsZe6SGCi8CY6dK1vEniFK3eZr0z17KiL0ncLxBEx2aw2v4RGL')
client_id = '211a42c6a16244ccb1f9142ae9cc7fc1'
client_secret = '2f65f549b398ecbbe047933822dc0c2fa950f67158e9e6bbddc256ff5beaebf6'
scopes = GsSession.Scopes.get_default()
GsSession.use(client_id = client_id, client_secret = client_secret, scopes = scopes)

def getSentiment(stocks):
	tickMap = getInfo(stocks.split(', '))
	stockMap = {}
	for tick in tickMap:
		tempMap = tickMap[tick]
		stockMap[(tempMap['name'])] = tick
	sentimentDict = {}
	infiniteCtr = 0
	bannedList = ['Inc', 'Corp', 'LLC', 'Co', "Ltd"]
	stockList = list(stockMap.keys())
	while(len(stockList) > 0):
		infiniteCtr += 1
		stock = stockList.pop()
		tempMap = tickMap[stockMap[stock]]
		num = tempMap['gsid']
		query = {'q': stock, 'result_type': 'popular', 'count': 100, 'lang': 'en'}
		sentimentScore = ctr = 0
		for status in twitter.search(**query)['statuses']:
			text = status['text']
			document = types.Document(
			    content=text,
			    type=enums.Document.Type.PLAIN_TEXT)

			# Detects the sentiment of the text
			sentiment = client.analyze_sentiment(document=document).document_sentiment
			sentimentScore = sentimentScore + (sentiment.score * sentiment.magnitude)
			ctr += 1
		if (infiniteCtr > 20):
			break

		if (ctr == 0):
			temp = stock.split()
			ban = False
			for word in bannedList:
				if word in temp:
					temp.remove(word)
					newStock = ''.join(temp)
					ban = True
					break
			if (ban):
				query = {'q': newStock, 'result_type': 'popular', 'count': 100, 'lang': 'en'}
				sentimentScore = sentimentMagnitude = ctr = 0
				for status in twitter.search(**query)['statuses']:
					text = status['text']
					document = types.Document(
					    content=text,
					    type=enums.Document.Type.PLAIN_TEXT)

					# Detects the sentiment of the text
					sentiment = client.analyze_sentiment(document=document).document_sentiment
					sentimentScore = sentimentScore + (sentiment.score * sentiment.magnitude)
					ctr += 1
			else:
				newStock = temp[0]
				query = {'q': newStock, 'result_type': 'popular', 'count': 100, 'lang': 'en'}
				sentimentScore = sentimentMagnitude = ctr = 0
				for status in twitter.search(**query)['statuses']:
					text = status['text']
					document = types.Document(
					    content=text,
					    type=enums.Document.Type.PLAIN_TEXT)

					# Detects the sentiment of the text
					sentiment = client.analyze_sentiment(document=document).document_sentiment
					sentimentScore = sentimentScore + (sentiment.score * sentiment.magnitude)
					ctr += 1
			if (ctr == 0):
				sentimentDict[num] = [0,0]
			else:
				sentimentDict[num] = sentimentScore / ctr	
		else:
			sentimentDict[num] = sentimentScore / ctr
	print(sentimentDict)
	return sentimentDict
