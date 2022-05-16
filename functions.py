def pressure_calc(target_psi, actual_psi):
    pressure_delta = target_psi - actual_psi
    return round(pressure_delta, 1)


def pressure_estimate(air_temp, actual_psi):
    pressure_delta_estimate = ((30 - air_temp) * 0.1) + actual_psi
    return pressure_delta_estimate


def seconds_from_midnight(input_secs):
    hours = int(input_secs / 60 / 60)
    minutes = int(input_secs / 60 % 60)
    seconds = int(input_secs % 60)
    output_time = str(hours) + ":" + str(minutes) + ":" + str(seconds)
    return output_time
