# bitcoin-graph
## Create the candlestick graph for Bitcoin using Coingecko API.
### We will use the API to get the price data for 30 days with 24 observation per day, 1 per hour. We will find the max, min, open, and close price per day meaning we will have 30 candlesticks and use that to generate the candlestick graph. Although we are using the CoinGecko API we will use a Python client/wrapper for the API called PyCoinGecko.
### PyCoinGecko will make performing the requests easy and it will deal with the endpoint targeting.

# Rest APIs
Rest API’s function by sending a request, the request is communicated via HTTP message. The HTTP message usually contains a JSON file. This contains instructions for what operation we would like the service or resource to perform. In a similar manner, API returns a response, via an HTTP message, this response is usually contained within a JSON.
In cryptocurrency a popular method to display the movements of the price of a currency is using candlestick.


![Screenshot (37)](https://user-images.githubusercontent.com/67437879/120457408-0b892900-c3b4-11eb-8545-c5ae03ed7651.png)

#### Here is a project demo in which the green candles shows the price closed higher than it opened and red candles shows the price closes lower than it opened. Each candlesticks describes the max, min, open, and close price per day.
![bitcoin_gif](https://user-images.githubusercontent.com/67437879/120456088-e9db7200-c3b2-11eb-8cc7-1be47f0658c2.gif)
