from datetime import date, datetime, timedelta
from gs_quant.data import Dataset
from gs_quant.markets.securities import SecurityMaster, AssetIdentifier
from gs_quant.session import GsSession

import pandas as pd
import pytz
import dateutil.relativedelta
import numpy as np
import csv
import random
import math

from stockTwitter import getSentiment
from stockGS import getInfo

client_id="211a42c6a16244ccb1f9142ae9cc7fc1"
client_secret="2f65f549b398ecbbe047933822dc0c2fa950f67158e9e6bbddc256ff5beaebf6"

# access marquee
scopes = GsSession.Scopes.get_default()
GsSession.use(client_id=client_id, client_secret=client_secret, scopes=scopes)
ds = Dataset('USCANFPP_MINI')
current_date = datetime.utcnow().replace(tzinfo=pytz.utc)

df = pd.read_csv('gs_sec_data.csv')
array = np.array(df[["gsid", "integratedScore"]])
totalVal = set()

def runClassifier(gsid):
    temp = []
    print(gsid)
    for elem in array:
        totalVal.add(elem[0])
        if len(temp) == 10:
            print(totalVal)
            return temp
        elif elem[0] == gsid:
            temp.append(elem[1])
    print(totalVal)
    return temp

def parseInputIntoCompanies(gsid):
    companyArr = []
    currElem = array[0][0]
    currCompany = []
    index = 0
    endIndex = len(array) - 1
    for elem in array:
        companyId = elem[0]
        while not isinstance(companyId, float):
            print(companyId)
            print(type(companyId))
            companyId = companyId[0]
        while not isinstance(companyId, float):
            companyId = companyId[0]
        if currElem == companyId:
            currCompany.append(elem[1])
            if index == endIndex:
                currCompany.append(elem[1])
                companyArr.append(currCompany)
                print(len(companyArr))
                break 
        else:       
            companyArr.append(currCompany)
            currElem = elem
            while not isinstance(currElem, float):
                currElem = currElem[0]
            currCompany = []
        index += 1
    return companyArr

def convertDataToLeastSquares(companyArr):
    dataSetLength = 10
    tenDayArr = []

    for company in companyArr:
        lengthCompanyData = len(company)
        index = 0
        for i in range(lengthCompanyData - dataSetLength):
            ok = True
            for j in range(dataSetLength + 1):
                if math.isnan(company[i + j]):
                    ok = False
                    break
            if (ok):
                tenDayArr.append([company[i:i+dataSetLength], company[i+dataSetLength]])
    
    trainingData = [data[0] for data in tenDayArr]
    trainingLabels = [data[1] for data in tenDayArr]

    testLeastSquares = np.linalg.lstsq(trainingData, trainingLabels)[0]
    return testLeastSquares

def classify(score):
    buy_score = 0.6
    sell_score = 0.2
    if score > buy_score:
        return 1
    elif score < sell_score:
        return -1
    else:
        return 0

runClassifier(14593)
