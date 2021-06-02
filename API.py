#delete on line ctrl+shft+k
#select on word in whole file ctrl+shift+l

import pandas as pd
import numpy as np
import datetime
import plotly.graph_objects as go
import plotly.offline as plot
import matplotlib.pyplot as plt
from pycoingecko import CoinGeckoAPI                        #although we are using coingecko API we will use a python client/wrapper for the API called pycoingecko
#                                                             PyCoinGecko will make performing the requests easy and it will deal with the enpoint targeting
from mplfinance.original_flavor import candlestick2_ohlc

# dict={'a':[1,5,8,8,9,6,3,1,4,8,0],'b':[8,7,3,8,7,9,4,9,7,6,2]}
# df=pd.DataFrame(dict)
# print(df)
# print(df.head())
# print(df.mean())


#coingeckoAPI to create candlestick graphs for BITCOIN
cg=CoinGeckoAPI()

# Using the get_coin_market_chart_by_id(id, vs_currency, days). id is the name of the coin you want, vs_currency is the currency you want the price in, and days is how many days back from today you want.
bitcoin=cg.get_coin_market_chart_by_id(id='bitcoin',vs_currency='usd',days=30)

# The response we get is in the form of a JSON which includes the price, market caps, and total volumes along with timestamps for each observation. We are focused on the prices so we will select that data.
bitcoin_price_data=bitcoin['prices']


# finally turn this data to pandas DataFrame with column name as timestamp and price
data =pd.DataFrame(bitcoin_price_data, columns=['Timestamp','Price'])
# print(data) 


# now we have a dataframe here we will convert the timestamp to datetime and save to a  new column added as date
data['Date']=pd.to_datetime(data['Timestamp'],unit='ms')
# print(data)

#Using the modified dataset we can now group by the Date and find the min, max, open, and close for the candlesticks
candlestick_data = data.groupby(data.Date.dt.date, as_index=False).agg({"Price": ['min', 'max', 'first', 'last']})
# print(candlestick_data)

#Finally we are now ready to use plotly to create our Candlestick Chart.
fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                open=candlestick_data['Price']['first'], 
                high=candlestick_data['Price']['max'],
                low=candlestick_data['Price']['min'], 
                close=candlestick_data['Price']['last'])
                ])

fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()