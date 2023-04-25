# This is a script for testing purposes - simply outputs to screen

from time import sleep
from functions import create_csv
from read_shared_memory import read_physics


if __name__ == '__main__':
    output_data = []
    polling_rate = 1    # Hz
    try:
        print("Started, press Ctrl+C to stop execution")
        while True:
            print(read_physics()["tyreTempI"][0])
            print(read_physics()["tyreTempM"][0])
            print(read_physics()["tyreTempO"][0])
            sleep(1 / polling_rate)
    except KeyboardInterrupt:
        print("Stopping")
        create_csv(output_data)
    