import numpy as np
from finrl.meta.preprocessor.preprocessors import FeatureEngineer, data_split

def add_features(df, technical_indicators):
    """
    Add features to the dataframe

    Args:
        df (pd.DataFrame): Dataframe of the stock data including date,open,high,low,close,volume,ticker,day
        technical_indicators (list): List of technical indicators to add to the dataframe

    Returns:
        df_processed (pd.DataFrame): Dataframe of the stock data including date,open,high,low,close,volume,ticker,day,technical indicators
    """
    fe = FeatureEngineer(use_technical_indicator=True,
                     tech_indicator_list = technical_indicators,
                     use_turbulence=True,
                     user_defined_feature = False)

    df_processed = fe.preprocess_data(df)
    df_processed = df_processed.copy()
    df_processed = df_processed.fillna(0)
    df_processed = df_processed.replace(np.inf,0)

    return df_processed