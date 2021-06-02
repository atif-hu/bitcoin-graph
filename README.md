# bitcoin-graph
Create the candlestick graph for Bitcoin using Coingecko API.
*We will use the API to get the price data for 30 days with 24 observation per day, 1 per hour. We will find the max, min, open, and close price per day meaning we will have 30 candlesticks and use that to generate the candlestick graph. Although we are using the CoinGecko API we will use a Python client/wrapper for the API called PyCoinGecko.
*PyCoinGecko will make performing the requests easy and it will deal with the endpoint targeting.
