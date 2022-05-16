from time import sleep
from read_shared_memory import read_graphics, read_physics, read_static


def main():
    if read_graphics()["ACC_STATUS"] == 1 or read_graphics()["ACC_STATUS"] == 2:
        if read_graphics()["iSplit"] < 300:
            stage_data = {
                # Basic Info
                "Track": read_static()["track"],
                "Car": read_static()["carModel"],
                "Session": read_graphics()["ACC_SESSION_TYPE"],
                # Laps and Times
                "CurrentSector": read_graphics()["currentSectorIndex"],
                "LapsCompleted": read_graphics()["completedLaps"],
                "BestLapTime": read_graphics()["iBestTime"],                    # unit: milliseconds
                "LastLapTime": read_graphics()["iLastTime"],                    # unit: milliseconds
                "LastSplitTime": read_graphics()["iSplit"],                     # unit: milliseconds
                # Weather Info
                "Clock": read_graphics()["Clock"],                              # unit: seconds from midnight
                "AmbientTemperature": read_physics()["airTemp"],                # unit: celsius
                "TrackTemperature": read_physics()["roadTemp"],                 # unit: celsius
                "GripStatus": read_graphics()["trackGripStatus"],
                "RainLevel": read_graphics()["rainIntensity"],
                "WindSpeed": read_graphics()["windSpeed"],                      # unit: m/s
                "WindDirection": read_graphics("windDirection"),                # unit: radians
                # Tyre Info
                "RainTyres": read_graphics()["rainTyres"],
                "TyreTemperatureFrontLeft": read_physics()["tyreCoreTemperature"][0],       # unit: celsius
                "TyreTemperatureFrontRight": read_physics()["tyreCoreTemperature"][1],      # unit: celsius
                "TyreTemperatureRearLeft": read_physics()["tyreCoreTemperature"][2],        # unit: celsius
                "TyreTemperatureRearRight": read_physics()["tyreCoreTemperature"][3],       # unit: celsius
                "TyrePressureFrontLeft": read_physics()["wheelPressure"][0],                # unit: psi
                "TyrePressureFrontRight": read_physics()["wheelPressure"][1],               # unit: psi
                "TyrePressureRearLeft": read_physics()["wheelPressure"][2],                 # unit: psi
                "TyrePressureRearRight": read_physics()["wheelPressure"][3],                # unit: psi
                # Electronics Settings Info
                "TractionControl": read_graphics()["TC"],
                "TractionControlCut": read_graphics()["TCCut"],
                "ABS": read_graphics()["ABS"],
                "BrakeBalance": read_physics()["brakeBias"],
                "EngineMap": read_graphics()["EngineMap"],
                # Fuel Data
                "CurrentFuel": read_physics()["fuel"],                          # unit: litres
                "UsedFuel": read_graphics()["usedFuel"],                        # unit: litres
                "FuelPerLap": read_graphics()["fuelXLap"],                      # unit: litres per lap
                "EstimatedFuelLaps": read_graphics()["fuelEstimatedLaps"],
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
