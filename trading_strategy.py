```python
import pandas as pd

# Convert data to pandas dataframe
df = pd.DataFrame(data['Time Series (1min)']).T
df.columns = ['open', 'high', 'low', 'close', 'volume']

# Convert columns to numeric types
df = df.apply(pd.to_numeric)

# Calculate moving averages
df['MA_20'] = df['close'].rolling(window=20).mean()
df['MA_50'] = df['close'].rolling(window=50).mean()

# Generate trading signals
df['signal'] = 0
df.loc[df['MA_20'] > df['MA_50'], 'signal'] = 1
df.loc[df['MA_20'] < df['MA_50'], 'signal'] = -1
```
