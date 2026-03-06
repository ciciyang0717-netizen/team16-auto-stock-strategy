import pandas as pd
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv('auto_stock_clean_data.csv')

df['Date'] = pd.to_datetime(df['Date'])
df.columns = df.columns.str.lower()

features = ['volatility_20d', 'momentum_20d', 'momentum_60d', 'rsi_14d']
df[features] = df.groupby('date')[features].rank(pct=True)
df[features] = df[features].fillna(0.5)

feature_cols = features
target_col = 'target_rank'
split_date = pd.to_datetime('2023-01-01')
train_mask = df['date'] < split_date
test_mask = df['date'] >= split_date

train_df = df[train_mask].copy()
test_df = df[test_mask].copy()

X_train = train_df[feature_cols]
y_train = train_df[target_col]

X_test = test_df[feature_cols]
y_test = test_df[target_col]

rf_model = RandomForestRegressor(
    n_estimators=200, 
    max_depth=2,         
    min_samples_leaf=3,  
    random_state=42
)
rf_model.fit(X_train, y_train)
test_df['predicted_rank'] = rf_model.predict(X_test)
test_df['signal'] = -test_df['predicted_rank']

print("\n" + "=" * 40)
print("Core Quant Metrics (Optimized Reversal Baseline)")
print("=" * 40)

print("\n[Feature Contributions]")
importances = rf_model.feature_importances_
for feature, imp in zip(feature_cols, importances):
    print(f"- {feature}: {imp:.1%}")

overall_ic = test_df[target_col].corr(test_df['signal'], method='spearman')
print(f"\n[Overall Rank IC (Reversal Signal)]: {overall_ic:.4f}")

daily_ic = test_df.groupby('date').apply(
    lambda g: g[target_col].corr(g['signal'], method='spearman')
)
print(f"[Daily Mean Rank IC]: {daily_ic.mean():.4f}, Std: {daily_ic.std():.4f}")