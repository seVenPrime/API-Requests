#Early get request
#To run: CTRL SHIFT B
import requests
response = requests.get('https://poloniex.com/public?command=returnTicker')
print (response.json())
