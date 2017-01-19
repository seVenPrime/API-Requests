#Early get request
#To run: CTRL SHIFT B
import requests
#command = "return24Volume"
payload = {'&currencyPair': 'btc:usd'}
command = "returnOrderBook"
URL = "https://poloniex.com/public?command=" + command + "&currencyPair=BTC_LTC"
response = requests.get(URL)
print (response.json())
