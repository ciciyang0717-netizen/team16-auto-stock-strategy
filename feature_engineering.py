import pandas as pd
df = pd.read_csv('auto_industry_data.csv')
df['momentum_20d'] = df.groupby('Ticker')['Adj Close'].pct_change(20)
df['momentum_60d'] = df.groupby('Ticker')['Adj Close'].pct_change(60)
df['Future_return_20d'] = (
    df.groupby('Ticker')['Adj Close'].shift(-20) / df['Adj Close'] - 1
)
df['Target_Rank'] = df.groupby('Date')['Future_return_20d'].rank(pct=True)

df_cleaned = df.dropna()

output_path = '/Users/ruhui/Desktop/data science society/sophia_features.csv'
df_cleaned.to_csv(output_path, index=False)

