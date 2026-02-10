import yfinance as yf
import pandas as pd


def main():
    # Tickers and date range
    tickers = ['TSLA', 'BYDDY', 'NIO', 'F', 'GM', 'TM', 'HMC', 'VWAGY', 'STLA']
    start_date = '2019-01-01'
    end_date = '2023-12-31'

    print("Downloading data from Yahoo Finance...")
    raw = yf.download(tickers, start=start_date, end=end_date)

    # We only keep 'Adj Close' and 'Volume'
    # yfinance may return a MultiIndex or a simple Index for columns
    if isinstance(raw.columns, pd.MultiIndex):
        # Level 0 usually contains the field names: 'Adj Close', 'Volume', etc.
        level0 = raw.columns.get_level_values(0)
        mask = level0.isin(['Adj Close', 'Volume'])
        data = raw.loc[:, mask].copy()
    else:
        # Single-level columns, just keep those that exist
        keep_cols = [c for c in ['Adj Close', 'Volume'] if c in raw.columns]
        data = raw[keep_cols].copy()

    # Validation: NaN counts
    total_nan = int(data.isna().sum().sum())
    print(f"\nTotal NaN values in dataset: {total_nan}")
    print("\nNaN count by column:")
    print(data.isna().sum())

    # Output: save to CSV
    output_file = 'auto_industry_data.csv'
    data.to_csv(output_file)

    # Print first 5 rows and shape
    print(f"\nData saved to: {output_file}")
    print("\nFirst 5 rows:")
    print(data.head())
    print("\nDataset shape (rows, columns):", data.shape)


if __name__ == '__main__':
    main()

