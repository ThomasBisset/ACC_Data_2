# up to date as of v1.8.12
# Code based on the work of dabde: https://github.com/dabde

from ctypes import Structure, sizeof, c_float, c_wchar, c_int
import mmap


class SPageFileStatic(Structure):
    _fields_ = [
        ("smVersion", c_wchar * 15),
        ("acVersion", c_wchar * 15),
        ("numberOfSessions", c_int),
        ("numCars", c_int),
        ("carModel", c_wchar * 33),
        ("track", c_wchar * 33),
        ("playerName", c_wchar * 33),
        ("playerSurname", c_wchar * 33),
        ("playerNick", c_wchar * 33),
        ("sectorCount", c_int),
        ("maxTorque", c_float),                                                                     # not used by ACC
        ("maxPower", c_float),                                                                      # not used by ACC
        ("maxRpm", c_int),
        ("maxFuel", c_float),
        ("suspensionMaxTravel", c_float * 4),                                                       # not used by ACC
        ("tyreRadius", c_float * 4),                                                                # not used by ACC
        ("maxTurboBoost", c_float * 4),                                                             # not used by ACC
        ("deprecated_1", c_float),                                                                  # not used by ACC
        ("deprecated_2", c_float),                                                                  # not used by ACC
        ("penaltiesEnabled", c_int),
        ("aidFuelRate", c_float),
        ("aidTireRate", c_float),
        ("aidMechanicalDamage", c_float),
        ("aidAllowTyreBlankets", c_int),
        ("aidStability", c_float),
        ("aidAutoClutch", c_int),
        ("aidAutoBlip", c_int),
        ("hasDRS", c_int),                                                                          # not used by ACC
        ("hasERS", c_int),                                                                          # not used by ACC
        ("hasKERS", c_int),                                                                         # not used by ACC
        ("kersMaxJ", c_float),                                                                      # not used by ACC
        ("engineBrakeSettingsCount", c_int),                                                        # not used by ACC
        ("ersPowerControllerCount", c_int),                                                         # not used by ACC
        ("trackSplineLength", c_float),                                                             # not used by ACC
        ("trackConfiguration", c_wchar * 33),                                                       # not used by ACC
        ("ersMaxJ", c_float),                                                                       # not used by ACC
        ("isTimedRace", c_int),                                                                     # not used by ACC
        ("hasExtraLap", c_int),                                                                     # not used by ACC
        ("carSkin", c_wchar * 33),                                                                  # not used by ACC
        ("reversedGridPositions", c_int),                                                           # not used by ACC
        ("PitWindowStart", c_int),
        ("PitWindowEnd", c_int),
        ("isOnline", c_int),
        ("dryTyresName", c_wchar * 33),
        ("wetTyresName", c_wchar * 33),
    ]


    def todict(self):
        return {
            "smVersion": self.smVersion,
            "acVersion": self.acVersion,
            "numberOfSessions": self.numberOfSessions,
            "numCars": self.numCars,
            "carModel": self.carModel,
            "track": self.track,
            "playerName": self.playerName,
            "playerSurname": self.playerSurname,
            "playerNick": self.playerNick,
            "sectorCount": self.sectorCount,
            "maxTorque": self.maxTorque,                                                            # not used by ACC
            "maxPower": self.maxPower,                                                              # not used by ACC
            "maxRpm": self.maxRpm,
            "maxFuel": self.maxFuel,
            "suspensionMaxTravel": self.suspensionMaxTravel,                                        # not used by ACC
            "tyreRadius": self.tyreRadius,                                                          # not used by ACC
            "maxTurboBoost": self.maxTurboBoost,                                                    # not used by ACC
            "deprecated_1": self.deprecated_1,                                                      # not used by ACC
            "deprecated_2": self.deprecated_2,                                                      # not used by ACC
            "penaltiesEnabled": self.penaltiesEnabled,
            "aidFuelRate": self.aidFuelRate,
            "aidTireRate": self.aidTireRate,
            "aidMechanicalDamage": self.aidMechanicalDamage,
            "aidAllowTyreBlankets": self.aidAllowTyreBlankets,
            "aidStability": self.aidStability,
            "aidAutoClutch": self.aidAutoClutch,
            "aidAutoBlip": self.aidAutoBlip,
            "hasDRS": self.hasDRS,                                                                  # not used by ACC
            "hasERS": self.hasERS,                                                                  # not used by ACC
            "hasKERS": self.hasKERS,                                                                # not used by ACC
            "kersMaxJ": self.kersMaxJ,                                                              # not used by ACC
            "engineBrakeSettingsCount": self.engineBrakeSettingsCount,                              # not used by ACC
            "ersPowerControllerCount": self.ersPowerControllerCount,                                # not used by ACC
            "trackSplineLength": self.trackSplineLength,                                            # not used by ACC
            "trackConfiguration": self.trackConfiguration,                                          # not used by ACC
            "ersMaxJ": self.ersMaxJ,                                                                # not used by ACC
            "isTimedRace": self.isTimedRace,                                                        # not used by ACC
            "hasExtraLap": self.hasExtraLap,                                                        # not used by ACC
            "carSkin": self.carSkin,                                                                # not used by ACC
            "reversedGridPositions": self.reversedGridPositions,                                    # not used by ACC
            "PitWindowStart": self.PitWindowStart,
            "PitWindowEnd": self.PitWindowEnd,
            "isOnline": self.isOnline,
            "dryTyresName": self.dryTyresName,
            "wetTyresName": self.wetTyresName,
        }


class SPageFileGraphic(Structure):
    _fields_ = [
        ("packetId", c_int),
        ("ACC_STATUS", c_int),
        ("ACC_SESSION_TYPE", c_int),
        ("currentTime", c_wchar * 15),
        ("lastTime", c_wchar * 15),
        ("bestTime", c_wchar * 15),
        ("split", c_wchar * 15),
        ("completedLaps", c_int),
        ("position", c_int),
        ("iCurrentTime", c_int),
        ("iLastTime", c_int),
        ("iBestTime", c_int),
        ("sessionTimeLeft", c_float),
        ("distanceTraveled", c_float),
        ("isInPit", c_int),
        ("currentSectorIndex", c_int),
        ("lastSectorTime", c_int),
        ("numberOfLaps", c_int),
        ("tyreCompound", c_wchar * 33),
        ("replayTimeMultiplier", c_float),                                                          # not used by ACC
        ("normalizedCarPosition", c_float),
        ("activeCars", c_int),
        ("carCoordinates", c_float * 60 * 3),
        ("carID", c_int * 60),
        ("playerCarID", c_int),
        ("penaltyTime", c_float),
        ("flag", c_int),
        ("penalty", c_int),
        ("idealLineOn", c_int),
        ("isInPitLane", c_int),
        ("surfaceGrip", c_float),
        ("mandatoryPitDone", c_int),
        ("windSpeed", c_float),
        ("windDirection", c_float),
        ("isSetupMenuVisible", c_int),
        ("mainDisplayIndex", c_int),
        ("secondaryDisplayIndex", c_int),
        ("TC", c_int),
        ("TCCut", c_int),
        ("EngineMap", c_int),
        ("ABS", c_int),
        ("fuelXLap", c_int),
        ("rainLights", c_int),
        ("flashingLights", c_int),
        ("lightsStage", c_int),
        ("exhaustTemperature", c_float),
        ("wiperLV", c_int),
        ("DriverStintTotalTimeLeft", c_int),
        ("DriverStintTimeLeft", c_int),
        ("rainTyres", c_int),
        ("sessionIndex", c_int),
        ("usedFuel", c_float),
        ("deltaLapTime", c_wchar * 15),
        ("iDeltaLapTime", c_int),
        ("estimatedLapTime", c_wchar * 15),
        ("iEstimatedLapTime", c_int),
        ("isDeltaPositive", c_int),
        ("iSplit", c_int),
        ("isValidLap", c_int),
        ("fuelEstimatedLaps", c_float),
        ("trackStatus", c_wchar * 33),
        ("missingMandatoryPits", c_int),
        ("Clock", c_float),
        ("directionLightsLeft", c_int),
        ("directionLightsRight", c_int),
        ("GlobalYellow", c_int),
        ("GlobalYellow1", c_int),
        ("GlobalYellow2", c_int),
        ("GlobalYellow3", c_int),
        ("GlobalWhite", c_int),
        ("GlobalGreen", c_int),
        ("GlobalChequered", c_int),
        ("GlobalRed", c_int),
        ("mfdTyreSet", c_int),
        ("mfdFuelToAdd", c_float),
        ("mfdTyrePressureLF", c_float),
        ("mfdTyrePressureRF", c_float),
        ("mfdTyrePressureLR", c_float),
        ("mfdTyrePressureRR", c_float),
        ("trackGripStatus", c_int),
        ("rainIntensity", c_int),
        ("rainIntensityIn10min", c_int),
        ("rainIntensityIn30min", c_int),
        ("currentTyreSet", c_int),
        ("strategyTyreSet", c_int),
        ("gapAhead", c_int),
        ("gapBehind", c_int),
    ]

    def todict(self):
        return {
            "packetId": self.packetId,
            "ACC_STATUS": self.ACC_STATUS,
            "ACC_SESSION_TYPE": self.ACC_SESSION_TYPE,
            "currentTime": self.currentTime,
            "lastTime": self.lastTime,
            "bestTime": self.bestTime,
            "split": self.split,
            "completedLaps": self.completedLaps,
            "position": self.position,
            "iCurrentTime": self.iCurrentTime,
            "iLastTime": self.iLastTime,
            "iBestTime": self.iBestTime,
            "sessionTimeLeft": self.sessionTimeLeft,
            "distanceTraveled": self.distanceTraveled,
            "isInPit": self.isInPit,
            "currentSectorIndex": self.currentSectorIndex,
            "lastSectorTime": self.lastSectorTime,
            "numberOfLaps": self.numberOfLaps,
            "tyreCompound": self.tyreCompound,
            "replayTimeMultiplier": self.replayTimeMultiplier,                                      # not used by ACC
            "normalizedCarPosition": self.normalizedCarPosition,
            "activeCars": self.activeCars,
            "carCoordinates": self.carCoordinates,
            "carID": self.carID,
            "playerCarID": self.playerCarID,
            "penaltyTime": self.penaltyTime,
            "flag": self.flag,
            "penalty": self.penalty,
            "idealLineOn": self.idealLineOn,
            "isInPitLane": self.isInPitLane,
            "surfaceGrip": self.surfaceGrip,
            "mandatoryPitDone": self.mandatoryPitDone,
            "windSpeed": self.windSpeed,
            "windDirection": self.windDirection,
            "isSetupMenuVisible": self.isSetupMenuVisible,
            "mainDisplayIndex": self.mainDisplayIndex,
            "secondaryDisplayIndex": self.secondaryDisplayIndex,
            "TC": self.TC,
            "TCCut": self.TCCut,
            "EngineMap": self.EngineMap,
            "ABS": self.ABS,
            "fuelXLap": self.fuelXLap,
            "rainLights": self.rainLights,
            "flashingLights": self.flashingLights,
            "lightsStage": self.lightsStage,
            "exhaustTemperature": self.exhaustTemperature,
            "wiperLV": self.wiperLV,
            "DriverStintTotalTimeLeft": self.DriverStintTotalTimeLeft,
            "DriverStintTimeLeft": self.DriverStintTimeLeft,
            "rainTyres": self.rainTyres,
            "sessionIndex": self.sessionIndex,
            "usedFuel": self.usedFuel,
            "deltaLapTime": self.deltaLapTime,
            "iDeltaLapTime": self.iDeltaLapTime,
            "estimatedLapTime": self.estimatedLapTime,
            "iEstimatedLapTime": self.iEstimatedLapTime,
            "isDeltaPositive": self.isDeltaPositive,
            "iSplit": self.iSplit,
            "isValidLap": self.isValidLap,
            "fuelEstimatedLaps": self.fuelEstimatedLaps,
            "trackStatus": self.trackStatus,
            "missingMandatoryPits": self.missingMandatoryPits,
            "Clock": self.Clock,
            "directionLightsLeft": self.directionLightsLeft,
            "directionLightsRight": self.directionLightsRight,
            "GlobalYellow": self.GlobalYellow,
            "GlobalYellow1": self.GlobalYellow1,
            "GlobalYellow2": self.GlobalYellow2,
            "GlobalYellow3": self.GlobalYellow3,
            "GlobalWhite": self.GlobalWhite,
            "GlobalGreen": self.GlobalGreen,
            "GlobalChequered": self.GlobalChequered,
            "GlobalRed": self.GlobalRed,
            "mfdTyreSet": self.mfdTyreSet,
            "mfdFuelToAdd": self.mfdFuelToAdd,
            "mfdTyrePressureLF": self.mfdTyrePressureLF,
            "mfdTyrePressureRF": self.mfdTyrePressureRF,
            "mfdTyrePressureLR": self.mfdTyrePressureLR,
            "mfdTyrePressureRR": self.mfdTyrePressureRR,
            "trackGripStatus": self.trackGripStatus,
            "rainIntensity": self.rainIntensity,
            "rainIntensityIn10min": self.rainIntensityIn10min,
            "rainIntensityIn30min": self.rainIntensityIn30min,
            "currentTyreSet": self.currentTyreSet,
            "strategyTyreSet": self.strategyTyreSet,
            "gapAhead": self.gapAhead,
            "gapBehind": self.gapBehind,
        }


class SPageFilePhysics(Structure):
    _fields_ = [
        ("packetId", c_int),
        ("gas", c_float),
        ("brake", c_float),
        ("fuel", c_float),
        ("gear", c_int),
        ("rpms", c_int),
        ("steerAngle", c_float),
        ("speedKmh", c_float),
        ("velocity", c_float * 3),
        ("accG", c_float * 3),
        ("wheelSlip", c_float * 4),
        ("wheelLoad", c_float * 4),                                                                 # not used by ACC
        ("wheelPressure", c_float * 4),
        ("wheelAngularSpeed", c_float * 4),
        ("tyreWear", c_float * 4),                                                                  # not used by ACC
        ("tyreDirtyLevel", c_float * 4),                                                            # not used by ACC
        ("tyreCoreTemperature", c_float * 4),
        ("camberRAD", c_float * 4),                                                                 # not used by ACC
        ("suspensionTravel", c_float * 4),
        ("drs", c_float),                                                                           # not used by ACC
        ("tc", c_float),
        ("heading", c_float),
        ("pitch", c_float),
        ("roll", c_float),
        ("cgHeight", c_float),                                                                      # not used by ACC
        ("carDamage", c_float * 5),
        ("numberOfTyresOut", c_int),                                                                # not used by ACC
        ("pitLimiterOn", c_int),
        ("abs", c_float),
        ("kersCharge", c_float),                                                                    # not used by ACC
        ("kersInput", c_float),                                                                     # not used by ACC
        ("autoShifterOn", c_int),
        ("rideHeight", c_float * 2),                                                                # not used by ACC
        ("turboBoost", c_float),
        ("ballast", c_float),                                                                       # not used by ACC
        ("airDensity", c_float),                                                                    # not used by ACC
        ("airTemp", c_float),
        ("roadTemp", c_float),
        ("localAngularVel", c_float * 3),
        ("finalFF", c_float),
        ("performanceMeter", c_float),                                                              # not used by ACC
        ("engineBrake", c_int),                                                                     # not used by ACC
        ("ersRecoveryLevel", c_int),                                                                # not used by ACC
        ("ersPowerLevel", c_int),                                                                   # not used by ACC
        ("ersHeatCharging", c_int),                                                                 # not used by ACC
        ("ersIsCharging", c_int),                                                                   # not used by ACC
        ("kersCurrentKJ", c_float),                                                                 # not used by ACC
        ("drsAvailable", c_int),                                                                    # not used by ACC
        ("drsEnabled", c_int),                                                                      # not used by ACC
        ("brakeTemp", c_float * 4),
        ("clutch", c_float),
        ("tyreTempI", c_float * 4),                                                                 # not shown in ACC
        ("tyreTempM", c_float * 4),                                                                 # not shown in ACC
        ("tyreTempO", c_float * 4),                                                                 # not shown in ACC
        ("isAIControlled", c_int),
        ("tyreContactPoint", c_float * 4 * 3),
        ("tyreContactNormal", c_float * 4 * 3),
        ("tyreContactHeading", c_float * 4 * 3),
        ("brakeBias", c_float),
        ("localVelocity", c_float * 3),
        ("P2PActivations", c_int),                                                                  # not used by ACC
        ("P2PStatus", c_int),                                                                       # not used by ACC
        ("currentMaxRpm", c_int),                                                                   # not used by ACC
        ("mz", c_float * 4),                                                                        # not used by ACC
        ("fx", c_float * 4),                                                                        # not used by ACC
        ("fy", c_float * 4),                                                                        # not used by ACC
        ("slipRatio", c_float * 4),
        ("slipAngle", c_float * 4),
        ("tcinAction", c_int),                                                                      # not used by ACC
        ("absInAction", c_int),                                                                     # not used by ACC
        ("suspensionDamage", c_float * 4),                                                          # not used by ACC
        ("tyreTemp", c_float * 4),                                                                  # not used by ACC
        ("waterTemp", c_float),
        ("brakePressure", c_float * 4),
        ("frontBrakeCompound", c_int),
        ("rearBrakeCompound", c_int),
        ("padLife", c_float * 4),
        ("discLife", c_float * 4),
        ("ignitionOn", c_int),
        ("starterEngineOn", c_int),
        ("EngineRunning", c_int),
        ("kerbVibration", c_float),
        ("slipVibrations", c_float),
        ("gVibrations", c_float),
        ("absVibrations", c_float),
    ]

    def todict(self):
        return {
            "packetId": self.packetId,
            "gas": self.gas,
            "brake": self.brake,
            "fuel": self.fuel,
            "gear": self.gear,
            "rpms": self.rpms,
            "steerAngle": self.steerAngle,
            "speedKmh": self.speedKmh,
            "velocity": self.velocity,
            "accG": self.accG,
            "wheelSlip": self.wheelSlip,
            "wheelLoad": self.wheelLoad,                                                            # not used by ACC
            "wheelPressure": self.wheelPressure,
            "wheelAngularSpeed": self.wheelAngularSpeed,
            "tyreWear": self.tyreWear,                                                              # not used by ACC
            "tyreDirtyLevel": self.tyreDirtyLevel,                                                  # not used by ACC
            "tyreCoreTemperature": self.tyreCoreTemperature,
            "camberRAD": self.camberRAD,                                                            # not used by ACC
            "suspensionTravel": self.suspensionTravel,
            "drs": self.drs,                                                                        # not used by ACC
            "tc": self.tc,
            "heading": self.heading,
            "pitch": self.pitch,
            "roll": self.roll,
            "cgHeight": self.cgHeight,                                                              # not used by ACC
            "carDamage": self.carDamage,
            "numberOfTyresOut": self.numberOfTyresOut,                                              # not used by ACC
            "pitLimiterOn": self.pitLimiterOn,
            "abs": self.abs,
            "kersCharge": self.kersCharge,                                                          # not used by ACC
            "kersInput": self.kersInput,                                                            # not used by ACC
            "autoShifterOn": self.autoShifterOn,
            "rideHeight": self.rideHeight,                                                          # not used by ACC
            "turboBoost": self.turboBoost,
            "ballast": self.ballast,                                                                # not used by ACC
            "airDensity": self.airDensity,                                                          # not used by ACC
            "airTemp": self.airTemp,
            "roadTemp": self.roadTemp,
            "localAngularVel": self.localAngularVel,
            "finalFF": self.finalFF,
            "performanceMeter": self.performanceMeter,                                              # not used by ACC
            "engineBrake": self.engineBrake,                                                        # not used by ACC
            "ersRecoveryLevel": self.ersRecoveryLevel,                                              # not used by ACC
            "ersPowerLevel": self.ersPowerLevel,                                                    # not used by ACC
            "ersHeatCharging": self.ersHeatCharging,                                                # not used by ACC
            "ersIsCharging": self.ersIsCharging,                                                    # not used by ACC
            "kersCurrentKJ": self.kersCurrentKJ,                                                    # not used by ACC
            "drsAvailable": self.drsAvailable,                                                      # not used by ACC
            "drsEnabled": self.drsEnabled,                                                          # not used by ACC
            "brakeTemp": self.brakeTemp,
            "clutch": self.clutch,
            "tyreTempI": self.tyreTempI,                                                            # not shown by ACC
            "tyreTempM": self.tyreTempM,                                                            # not shown by ACC
            "tyreTempO": self.tyreTempO,                                                            # not shown by ACC
            "isAIControlled": self.isAIControlled,
            "tyreContactPoint": self.tyreContactPoint,
            "tyreContactNormal": self.tyreContactNormal,
            "tyreContactHeading": self.tyreContactHeading,
            "brakeBias": self.brakeBias,
            "localVelocity": self.localVelocity,
            "P2PActivations": self.P2PActivations,                                                  # not used by ACC
            "P2PStatus": self.P2PStatus,                                                            # not used by ACC
            "currentMaxRpm": self.currentMaxRpm,                                                    # not used by ACC
            "mz": self.mz,                                                                          # not used by ACC
            "fx": self.fx,                                                                          # not used by ACC
            "fy": self.fy,                                                                          # not used by ACC
            "slipRatio": self.slipRatio,
            "slipAngle": self.slipAngle,
            "tcinAction": self.tcinAction,                                                          # not used by ACC
            "absInAction": self.absInAction,                                                        # not used by ACC
            "suspensionDamage": self.suspensionDamage,                                              # not used by ACC
            "tyreTemp": self.tyreTemp,                                                              # not used by ACC
            "waterTemp": self.waterTemp,
            "brakePressure": self.brakePressure,
            "frontBrakeCompound": self.frontBrakeCompound,
            "rearBrakeCompound": self.rearBrakeCompound,
            "padLife": self.padLife,
            "discLife": self.discLife,
            "ignitionOn": self.ignitionOn,
            "starterEngineOn": self.starterEngineOn,
            "EngineRunning": self.EngineRunning,
            "kerbVibration": self.kerbVibration,
            "slipVibrations": self.slipVibrations,
            "gVibrations": self.gVibrations,
            "absVibrations": self.absVibrations,
        }


def read_physics():
    buf = mmap.mmap(-1, sizeof(SPageFilePhysics), u"Local\\acpmf_physics")
    data = SPageFilePhysics.from_buffer(buf)
    return data.todict()


def read_static():
    buf = mmap.mmap(-1, sizeof(SPageFileStatic), u"Local\\acpmf_static")
    data = SPageFileStatic.from_buffer(buf)
    return data.todict()


def read_graphics():
    buf = mmap.mmap(-1, sizeof(SPageFileGraphic), u"Local\\acpmf_graphics")
    data = SPageFileGraphic.from_buffer(buf)
    return data.todict()
