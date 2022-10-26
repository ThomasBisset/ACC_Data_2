import datetime
import time
import pandas as pd


def lap_time_converter(milliseconds):
    if milliseconds == 2147483647:
        return "NULL"
    else:
        secs = milliseconds / 1000
        output_time = datetime.timedelta(seconds=secs)
        return output_time


def create_csv(input_df):
    filename = "ACC-Data-" + time.strftime("%Y-%m-%d-%H-%M-%S") + ".csv"
    df = pd.DataFrame(input_df)
    cleaned_df = df[df["SessionStatus"] == 2]
    pd.DataFrame(cleaned_df).to_csv(filename)
    print("Writing to CSV file - " + filename)
