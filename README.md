# Ticker Picker
**What is it**

Ticker Picker is an application that recommends what to do with a stock based on previous market data and sentiment analysis on Tweets related to that stock. The core of our application is a recurrent neural network which is trained on old market data from the Goldman Sachs Marquee API. The neural network combines this data with additional information from sentiment analysis that we ran on the top tweets of the stock name. The output of the neural network is fed through a softmax function which ultimately classifies the stock into one of three categories: buy, hold, or sell. The functionality of the programming is currently unavaliable because our Hackathon API tokens have expired.  
Back-end endpoint: https://tickerpicker.appspot.com

**How does it work**

Our program takes in as input a stock ticker name. Using the Marquee API, we can map this ticker to the company's actual name. We trained a RNN with old data of this ticker name and then use the most recent 10 days of data to predict whether the stock will increase. We took  For sentiment analysis, we find the most popular tweets from the last 30 days relating to the company name via the Twitter Standard Api. We then run sentiment analysis on each tweet through Google's Natural Language API and compute the average of the scores multiplied by the magnitudes. The final score reflects the overall sentiment of the company. We add this score to the number outputted by the neural network and then classify it as either buy, hold, or sell based on our estimates. 

**What's next**

We hope to train our model for better accuracy by using more recent data since the API we used only had data from the years 2012 to 2017. We also would like to do more research on how neural networks are used in financial modeling, and update our program based on the results. The sentiment analysis could also be further improved in our program by incorporating more social media and news platforms beyond just Twitter.  

