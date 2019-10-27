from datetime import date, datetime, timedelta
from gs_quant.data import Dataset
from gs_quant.markets.securities import SecurityMaster, AssetIdentifier
from gs_quant.session import GsSession

import pandas as pd
import pytz
import dateutil.relativedelta
import numpy as np

from stockTwitter import getSentiment
from stockGS import getInfo
from leastsquares import parseInputIntoCompanies, convertDataToLeastSquares, classify, runClassifier

def mainfn(ticker):
	ticker = ticker.upper()
	s = ticker.split()
	# for st in s:
	tickerMap = getInfo(ticker)
	temp = tickerMap[ticker]
	gsid = temp['gsid']
	ticker_dict = getSentiment(ticker)
	print(ticker_dict)
	ticker_score = ticker_dict[gsid] * 10
	companyArr = parseInputIntoCompanies(gsid) #trains the model
	leastSquaresModel = convertDataToLeastSquares(companyArr) #gets the least squares function

	print(leastSquaresModel)

	#get the last 10 days worth
	last_10 = runClassifier(gsid)
	print(last_10)

	next_day_prediction = np.dot(leastSquaresModel, last_10)

	overall_score = ticker_score * next_day_prediction

	classifier = classify(overall_score)

	return last_10, ticker_score, classifier

print(mainfn('FISV'))

