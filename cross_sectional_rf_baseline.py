import pandas as pd
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv('/Users/ruhui/Desktop/data science society/auto_stock_clean_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
split_date = '2023-01-01'

train_mask = df['Date'] < split_date
test_mask = df['Date'] >= split_date

train_df = df[train_mask]
test_df = df[test_mask]

feature_cols = ['momentum_20d', 'momentum_60d', 'volatility_20d', 'rsi_14d']
target_col = 'target_rank'

X_train = train_df[feature_cols]
y_train = train_df[target_col]

X_test = test_df[feature_cols]
y_test = test_df[target_col]

print(f"Training set features shape: {X_train.shape}, Target shape: {y_train.shape}")
print(f"Test set features shape: {X_test.shape}, Target shape: {y_test.shape}")

rf_model = RandomForestRegressor(
    n_estimators=100,  
    max_depth=5,       
    random_state=16   
)
rf_model.fit(X_train, y_train)
y_pred = rf_model.predict(X_test)

test_df = test_df.copy()
test_df['Predicted_Rank'] = y_pred

print("\nModel prediction completed! Here are the predicted ranks for the first 5 days:")
print(test_df[['Date', 'Ticker', 'target_rank', 'Predicted_Rank']].head())


import scipy.stats as stats

print("\n" + "="*40)
print("Core Quant Metrics")
print("="*40)

print("\n[Feature Contributions]")
importances = rf_model.feature_importances_
for feature, imp in zip(feature_cols, importances):
    print(f"- {feature}: {imp:.1%}")

ic_value = test_df['target_rank'].corr(test_df['Predicted_Rank'], method='spearman')
print(f"\n[Overall Model Rank IC]: {ic_value:.4f}")