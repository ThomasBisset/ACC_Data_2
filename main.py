from time import sleep
from read_shared_memory import read_graphics, read_physics, read_static


def main():
    if read_graphics()["ACC_STATUS"] == 1 or read_graphics()["ACC_STATUS"] == 2:
        if read_graphics()["iSplit"] < 300:
            stage_data = {
                # Basic info
                "Track": read_static()["track"],
                "Car": read_static()["carModel"],
                "Session": read_graphics()["ACC_SESSION_TYPE"],
                # Weather Info
                "Clock": read_graphics()["Clock"],
                "AmbientTemperature": read_physics()["airTemp"],
                "TrackTemperature": read_physics()["roadTemp"],
                
            }
    return stage_data


if __name__ == '__main__':
    try:
        print("Starting")
        while True:
            main()
            sleep(0.5)
    except KeyboardInterrupt:
        print("Exiting")
