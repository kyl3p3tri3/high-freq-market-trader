# high-freq-market-trader
# credit to chatGPT 3.5 for step by step outline and example code.
# credit to Hummingbot (https://www.youtube.com/watch?v=M9YfyL2icaQ&list=PLjb8cayyw0H81VrhzzhFS8am90xpYDx-S&index=12)

# Step 1: Set Up Environment
Start by setting up your Python environment and installing the necessary libraries. Some commonly used libraries for algorithmic trading include pandas, numpy, matplotlib, requests, and websocket-client.

# Step 2: Connect to a Data Source
To trade stocks, you need market data. There are various data providers available that provide historical and real-time market data. You can choose a provider and connect to their API to retrieve the required data. 


# Step 3: Implement Trading Strategy
Define your trading strategy based on the market data you retrieve. This can involve technical indicators, statistical analysis, or machine learning algorithms. 

  Strategies to implement:
  - Pure Market Making
      Description:
        Provides liquidity around the mid-price and tries to capture the                       volatility. It uses pairs of limit orders.

      Risks:
        Price risk of holding the asset.
        Inventory risk.
              
  - Arbitrage
      Description:
       Finds inefficiencies between markets, and tries to buy low in one exchange and         sell high in another. It is a taker strategy and uses two market orders.

      Risks:
       Price risk of holding the asset.


  - Cross Exchange Market Making
      Description:
        Provides liquidity in a market with low liquidity and high spread and hedges           the trades in a market with higher liquidity and lower spread. Places two              limit orders in a low liquid market and buys market in the other when one              order is executed.

      Risks:
       Price risk of holding the asset.
    

# Step 4: Execute Trades
After generating trading signals, you need to send orders to the market. This step requires integration with a brokerage or trading platform that allows programmatic access to execute trades.

