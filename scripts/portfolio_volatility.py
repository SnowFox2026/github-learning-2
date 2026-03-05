import pandas as pd

returns = pd.read_csv("returns.csv")

volatility = returns.std()

print(volatility)
