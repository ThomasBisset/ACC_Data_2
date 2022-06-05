import time
import pandas as pd


def seconds_from_midnight(input_secs):
    hours = int(input_secs / 60 / 60)
    minutes = int(input_secs / 60 % 60)
    seconds = int(input_secs % 60)
    output_time = str(hours) + ":" + str(minutes) + ":" + str(seconds)
    return output_time


def lap_time_error_handler(lap_time):
    if lap_time == 2147483647:
        return "NULL"
    else:
        return lap_time


def create_csv(data):
    filename = time.strftime("%Y-%m-%d-%H-%M-%S") + ".csv"
    pd.DataFrame(data).to_csv(filename)
