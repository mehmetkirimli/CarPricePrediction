import pandas as pd

data_path = "data/vehicle_price_prediction.csv"

def load_data():
    df = pd.read_csv(data_path)
    return df
