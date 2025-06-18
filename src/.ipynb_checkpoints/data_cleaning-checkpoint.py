import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def clean_data(df):
    # Drop duplicates
    df = df.drop_duplicates()

    # Fill missing values (example: forward fill)
    df = df.fillna(method='ffill')

    return df

def save_cleaned_data(df, output_path):
    df.to_csv(output_path, index=False)
