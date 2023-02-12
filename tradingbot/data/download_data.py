from finrl.config_tickers import DOW_30_TICKER
from finrl.meta.preprocessor.yahoodownloader import YahooDownloader
import argparse

def download_data(start_date, end_date):
    df = YahooDownloader(start_date = start_date,
                         end_date = end_date,
                         ticker_list = DOW_30_TICKER).fetch_data()

    return df

def download_data_command():
    """Download data from Yahoo Finance and save to a csv file
    
    Returns:
        df (pd.DataFrame): Dataframe of the stock data including date,open,high,low,close,volume,ticker,day
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--start_date", default = "2010-01-01", help = "start date")
    parser.add_argument("--end_date", default = "2021-01-01", help = "end date")
    args = parser.parse_args()

    df = download_data(start_date = args.start_date,
                         end_date = args.end_date)

    return df
