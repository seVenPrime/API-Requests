#Early get request
#To run: CTRL SHIFT B
import requests
command = "returnTradeHistory" #No market in name
URL = "https://poloniex.com/public?command=" + command + "&currencyPair=BTC_LTC"
response = requests.get(URL)
print (response.json())
