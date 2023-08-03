```python
import requests

# API key from Alpha Vantage
api_key = 'YOUR_API_KEY'

# Symbol and time interval for data retrieval
symbol = 'AAPL'
interval = '1min'

# Retrieve historical data
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={api_key}'
response = requests.get(url)
data = response.json()
```


