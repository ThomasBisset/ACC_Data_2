import time
import pandas as pd


def create_csv(input_df):
    filename = "ACC-Data-" + time.strftime("%Y-%m-%d-%H-%M-%S") + ".csv"
    df = pd.DataFrame(input_df)
    cleaned_df = df[df["SessionStatus"] == 2]
    pd.DataFrame(cleaned_df).to_csv(filename)
    print("Writing to CSV file - " + filename)

