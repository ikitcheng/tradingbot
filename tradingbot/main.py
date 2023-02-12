from data.download_data import download_data
from preprocess.preprocess import add_features
from config import config_folders

if __name__ == '__main__':
    # Configure folders
    config_folders()

    # Download data
    TRAIN_START_DATE = '2009-04-01'
    TRAIN_END_DATE = '2021-01-01'
    TEST_START_DATE = '2021-01-01'
    TEST_END_DATE = '2022-06-01'
    df = download_data(start_date = TRAIN_START_DATE, end_date = TEST_END_DATE)
    print(df.head())

    # Add features
    INDICATORS = ['macd',
               'rsi_30',
               'cci_30',
               'dx_30']
    df_processed = add_features(df, INDICATORS)
    print(df_processed.head())
