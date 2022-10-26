from time import sleep
from functions import create_csv
from data_collection import data_collection


if __name__ == '__main__':
    output_data = []
    polling_rate = 1    # Hz
    try:
        print("Started, press Ctrl+C to stop execution")
        while True:
            output_data.append(data_collection())
            sleep(1 / polling_rate)
    except KeyboardInterrupt:
        print("Stopping")
        create_csv(output_data)
    