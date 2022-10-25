from read_shared_memory import read_graphics, read_physics, read_static
from functions import lap_time_error_handler


def data_collection():
    data = {
        # Basic Info
        "Track": read_static()["track"],
        "Car": read_static()["carModel"],
        "Session": read_graphics()["ACC_SESSION_TYPE"],
        "Flag": read_graphics()["flag"],
        "Penalty": read_graphics()["penalty"],
        "InPit": read_graphics()["isInPit"],
        "InPitLane": read_graphics()["isInPitLane"],
        # Laps and Times
        "CurrentSector": read_graphics()["currentSectorIndex"],
        "LapsCompleted": read_graphics()["completedLaps"],
        "BestLapTime": lap_time_error_handler(read_graphics()["iBestTime"]),                # unit: milliseconds
        "LastLapTime": lap_time_error_handler(read_graphics()["iLastTime"]),                # unit: milliseconds
        "LastSplitTime": read_graphics()["iSplit"],                                         # unit: milliseconds
        "TrackPosition": read_graphics()["normalizedCarPosition"],
        # Weather Info
        "Clock": read_graphics()["Clock"],                                                  # unit: seconds from 00:00
        "AmbientTemperature": round(read_physics()["airTemp"], 3),                          # unit: celsius
        "TrackTemperature": round(read_physics()["roadTemp"], 3),                           # unit: celsius
        "GripStatus": read_graphics()["trackGripStatus"],
        "RainLevel": read_graphics()["rainIntensity"],
        "WindSpeed": round(read_graphics()["windSpeed"], 3),                                # unit: m/s
        "WindDirection": round(read_graphics()["windDirection"], 3),                        # unit: radians
        # Tyre Info
        "RainTyres": read_graphics()["rainTyres"],
        "TyreTemperatureFrontLeft": round(read_physics()["tyreCoreTemperature"][0], 3),     # unit: celsius
        "TyreTemperatureFrontRight": round(read_physics()["tyreCoreTemperature"][1], 3),    # unit: celsius
        "TyreTemperatureRearLeft": round(read_physics()["tyreCoreTemperature"][2], 3),      # unit: celsius
        "TyreTemperatureRearRight": round(read_physics()["tyreCoreTemperature"][3], 3),     # unit: celsius
        "TyrePressureFrontLeft": round(read_physics()["wheelPressure"][0], 3),              # unit: psi
        "TyrePressureFrontRight": round(read_physics()["wheelPressure"][1], 3),             # unit: psi
        "TyrePressureRearLeft": round(read_physics()["wheelPressure"][2], 3),               # unit: psi
        "TyrePressureRearRight": round(read_physics()["wheelPressure"][3], 3),              # unit: psi
        # Electronics Settings Info
        "TractionControl": read_graphics()["TC"],
        "TractionControlCut": read_graphics()["TCCut"],
        "EngineMap": read_graphics()["EngineMap"],
        # Brakes Data
        "BrakeTemperatureFrontLeft": round(read_physics()["brakeTemp"][0], 3),              # unit: celsius
        "BrakeTemperatureFrontRight": round(read_physics()["brakeTemp"][0], 3),             # unit: celsius
        "BrakeTemperatureRearLeft": round(read_physics()["brakeTemp"][0], 3),               # unit: celsius
        "BrakeTemperatureRearRight": round(read_physics()["brakeTemp"][0], 3),              # unit: celsius
        "BrakeBalance": round(read_physics()["brakeBias"], 3),
        "ABS": read_graphics()["ABS"],
        "FrontBrakeCompound": read_physics()["frontBrakeCompound"],
        "RearBrakeCompound": read_physics()["rearBrakeCompound"],
        # Fuel Data
        "CurrentFuel": round(read_physics()["fuel"], 3),                                    # unit: litres
        "UsedFuel": round(read_graphics()["usedFuel"], 3),                                  # unit: litres
        "FuelPerLap": round(read_graphics()["fuelXLap"], 3),                                # unit: litres per lap
        "EstimatedFuelLaps": round(read_graphics()["fuelEstimatedLaps"], 3),
    }
    return data
