# Aurora's Feature Engineering - Module 2

## 📊 Calculated Factors
- **20-day Volatility (Volatility_20d)**: Standard deviation of daily returns over the past 20 trading days
- **14-day RSI (Relative Strength Index)**: 14-day relative strength index

## 📁 File Description
- `aurora_features.csv` - Final output file (contains Date, Ticker, Volatility_20d, RSI_14d)
- `aurora_calc.py` - Python script for factor calculation
- `auto_industry_data.xlsx` - Raw data file (9 stocks, 2019-2023)

## 🔧 Environment Requirements
- Python 3.x
- Required packages: pandas, openpyxl, numpy

## 📈 Output Preview
| Date | Ticker | Volatility_20d | RSI_14d |
|------|--------|----------------|---------|
| 2019-01-02 | BYDDY | NaN | NaN |
| 2019-01-03 | BYDDY | NaN | 0.00 |
| 2019-01-04 | BYDDY | NaN | 10.50 |

> ⚠️ **Note**: First 20 rows of Volatility_20d are NaN, first 14 rows of RSI_14d are NaN. This is normal and expected as we need enough data points to calculate these indicators.

## 🎯 Next Steps
Hand over to Cici for:
1. Data cleaning (dropna())
2. Z-Score standardization
3. Correlation heatmap analysis

## 📅 Time Period
- 2019-01-02 to 2023-12-29
- 9 stocks in universe (BYDDY, F, GM, HMC, NIO, STLA, TM, TSLA, VWAGY)

## 👩‍💻 Author
Aurora - Module 2 (Time Series Indicators)

## 📊 Factor Calculation Details

### 20-day Volatility
```python
# Calculated using rolling 20-day standard deviation of daily returns
df['Volatility_20d'] = df.groupby('Ticker')['Return'].rolling(window=20).std()