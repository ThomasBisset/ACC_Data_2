from time import sleep
from read_shared_memory import read_graphics
from functions import create_csv
from data_collection import data_collection
import numpy as np


if __name__ == '__main__':
    output_data = []
    try:
        print("Starting")
        while True:
            if read_graphics()["ACC_STATUS"] == 2 and 250 < read_graphics()["iSplit"] < 500:
                output_data.append(data_collection())
                sleep(0.5)

    except KeyboardInterrupt:
        print("Stopping")
        create_csv(output_data)
        print("Writing " + str(np.array(output_data).size) + " rows to CSV file")
