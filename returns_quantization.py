import sys

import pandas as pd

from data_manager import file_processor
from utils import compute_returns


def add_returns_in_place(df):  # modifies df
    close_prices_returns = compute_returns(df)
    num_bins = 10
    returns_bins = pd.cut(close_prices_returns, num_bins)
    bins_categories = returns_bins.values.categories
    returns_labels = pd.cut(close_prices_returns, num_bins, labels=False)

    df['close_price_returns'] = close_prices_returns
    df['close_price_returns_bins'] = returns_bins
    df['close_price_returns_labels'] = returns_labels

    return df, bins_categories


def generate_bins(data_folder, bitcoin_file):
    p = file_processor(bitcoin_file)
    add_returns_in_place(p)


def main():
    arg = sys.argv
    assert len(arg) == 3, 'Usage: python3 {} DATA_FOLDER_TO_STORE_GENERATED_DATASET ' \
                          'BITCOIN_MARKET_DATA_CSV_PATH'.format(arg[0])
    data_folder = arg[1]
    bitcoin_file = arg[2]
    generate_bins(data_folder, bitcoin_file)


if __name__ == '__main__':
    main()