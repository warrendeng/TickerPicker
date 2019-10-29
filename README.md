# Ticker Picker
**What is it**

Ticker Picker is an application that recommends what to do with a stock based on previous market data and sentiment analysis on Tweets related to that stock. The core of our application is a recurrent neural network which is trained on old market data from the Goldman Sachs Marquee API. The neural network combines this data with additional information from sentiment analysis that we ran on the top tweets of the stock name using Google's Cloud Natural Language API and Twitter's Standard API. The output of the neural network is fed through a softmax function which ultimately classifies the stock into one of three categories: buy, hold, or sell. The Marquee API that was provided to us only had data up to 2017, but we hope that with more current data, our application would better predict how a stock will trend. The functionality of the programming is currently unavaliable because our Hackathon API tokens have expired.  
Back-end endpoint: https://tickerpicker.appspot.com

**How does it work**


**What's next**

We hope to train our model for better accuracy by using more recent data since the API we used only had data from the years 2012 to 2017. We also would like to do more research on how neural networks are used in financial modeling, and update our program based on the results. The sentiment analysis could also be further improved in our program by incorporating more social media and news platforms beyond just Twitter.  

