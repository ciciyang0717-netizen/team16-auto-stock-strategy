# Aurora's script to calculate 20-day volatility and 14-day RSI

print("=" * 50)
print("Aurora's Factor Calculation Program")
print("=" * 50)

# 1. Import required libraries
import pandas as pd
import numpy as np

# 2. Load the Excel file
print("\n📂 Reading data file...")
df = pd.read_excel('auto_industry_data.xlsx')
print(f"✅ Successfully loaded {len(df)} rows")

# 3. Sort by Ticker and Date to ensure correct order
df = df.sort_values(['Ticker', 'Date']).reset_index(drop=True)

# 4. Calculate daily returns (needed for volatility)
print("\n📊 Calculating factors...")
df['Return'] = df.groupby('Ticker')['Adj Close'].pct_change()

# 5. Calculate 20-day volatility (rolling standard deviation)
print("   - Calculating 20-day volatility...")
df['Volatility_20d'] = df.groupby('Ticker')['Return'].rolling(window=20).std().reset_index(level=0, drop=True)

# 6. Calculate 14-day RSI
print("   - Calculating 14-day RSI...")
def calculate_rsi(group):
    delta = group['Adj Close'].diff()
    gain = delta.clip(lower=0)
    loss = (-delta).clip(lower=0)
    avg_gain = gain.ewm(span=14, adjust=False).mean()
    avg_loss = loss.ewm(span=14, adjust=False).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    rsi = rsi.where(avg_loss != 0, 100.0)   # when avg_loss is 0, RSI = 100
    return rsi

df['RSI_14d'] = df.groupby('Ticker', group_keys=False).apply(calculate_rsi)

# 7. Keep only the columns needed for output
result = df[['Date', 'Ticker', 'Volatility_20d', 'RSI_14d']].copy()

# 8. Save to CSV
result.to_csv('aurora_features.csv', index=False)

print("\n✅ Done! File saved as: aurora_features.csv")
print("\n👀 Preview (first 10 rows):")
print(result.head(10))
