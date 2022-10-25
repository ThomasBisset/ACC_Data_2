def flag_type(enum):
    flag = {
        0: "No Flag",
        1: "Blue Flag",
        2: "Yellow Flag",
        3: "Black Flag",
        4: "White Flag",
        5: "Chequered Flag",
        6: "Penalty Flag",
        7: "Green Flag",
        8: "Orange Flag"
    }
    return flag[enum]


def penalty_type(enum):
    penalty = {
        0: "No Penalty",
        1: "Drive Through Penalty (Track Limits)",
        2: "10s Stop & Go Penalty (Track Limits)",
        3: "20s Stop & Go Penalty (Track Limits)",
        4: "30s Stop & Go Penalty (Track Limits)",
        5: "Disqualified (Track Limits)",
        6: "Lap Time Deleted (Track Limits)",
        7: "Drive Through Penalty (Speeding in the Pit Lane)",
        8: "10s Stop & Go Penalty (Speeding in the Pit Lane)",
        9: "20s Stop & Go Penalty (Speeding in the Pit Lane)",
        10: "30s Stop & Go Penalty (Speeding in the Pit Lane)",
        11: "Disqualified (Speeding in the Pit Lane)",
        12: "Lap Time Deleted (Speeding in the Pit Lane)",
        13: "Disqualified (Ignored Mandatory Pit Stop)",
        14: "Post Race Time Penalty",
        15: "Disqualified (Unsportsmanlike Conduct)",
        16: "Disqualified (Pit Entry)",
        17: "Disqualified (Pit Exit)",
        18: "Disqualified (Driving the Wrong Way)",
        19: "Drive Through (Ignored Driver Stint Limit)",
        20: "Disqualified (Ignored Driver Stint Limit)",
        21: "Disqualified (Exceeded Driver Stint Limit)"
    }
    return penalty[enum]


def session_type(enum):
    session = {
        -1: "Unknown",
        0: "Practice",
        1: "Qualifying",
        2: "Race",
        3: "Hotlap",
        4: "Time Attack",
        5: "Drift",
        6: "Drag",
        7: "Hot Stint",
        8: "Hot Stint Superpole"
    }
    return session[enum]


def session_status(enum):
    status = {
        0: "Off",
        1: "Replay",
        2: "Live",
        3: "Pause"
    }
    return status[enum]


def wheels_type(enum):
    wheel = {
        0: "Front Left",
        1: "Front Right",
        2: "Rear Left",
        3: "Rear Right"
    }
    return wheel[enum]


def track_grip_status(enum):
    grip_status = {
        0: "Green",
        1: "Fast",
        2: "Optimum",
        3: "Greasy",
        4: "Damp",
        5: "Wet",
        6: "Flooded"
    }
    return grip_status[enum]


def rain_intensity(enum):
    rain = {
        0: "No Rain",
        1: "Drizzle",
        2: "Light Rain",
        3: "Medium Rain",
        4: "Heavy Rain",
        5: "Thunderstorm"
    }
    return rain[enum]


def car_model(enum):
    car = {
        # GT3 - 2018
        "amr_v12_vantage_gt3": "Aston Martin Vantage V12 GT3 2013",
        "audi_r8_lms": "Audi R8 LMS 2015",
        "bentley_continental_gt3_2016": "Bentley Continental GT3 2015",
        "bentley_continental_gt3_2018": "Bentley Continental GT3 2018",
        "bmw_m6_gt3": "BMW M6 GT3 2017",
        "jaguar_g3": "Emil Frey Jaguar G3 2012",
        "ferrari_488_gt3": "Ferrari 488 GT3 2018",
        "honda_nsx_gt3": "Honda NSX GT3 2017",
        "lamborghini_gallardo_rex": "Lamborghini Gallardo G3 Reiter 2017",
        "lamborghini_huracan_gt3": "Lamborghini Huracan GT3 2015",
        "lamborghini_huracan_st": "Lamborghini Huracan ST 2015",
        "lexus_rc_f_gt3": "Lexus RCF GT3 2016",
        "mclaren_650s_gt3": "McLaren 650S GT3 2015",
        "mercedes_amg_gt3": "Mercedes AMG GT3 2015",
        "nissan_gt_r_gt3_2017": "Nissan GTR Nismo GT3 2015",
        "nissan_gt_r_gt3_2018": "Nissan GTR Nismo GT3 2018",
        "porsche_991_gt3_r": "Porsche 991 GT3 R 2018",
        "porsche_991ii_gt3_cup": "Porsche 991 II GT3 Cup 2017",
        # GT3 - 2019
        "amr_v8_vantage_gt3": "Aston Martin V8 Vantage GT3 2019",
        "audi_r8_lms_evo": "Audi R8 LMS Evo 2019",
        "honda_nsx_gt3_evo": "Honda NSX GT3 Evo 2019",
        "lamborghini_huracan_gt3_evo": "Lamborghini Huracan GT3 EVO 2019",
        "mclaren_720s_gt3": "McLaren 720S GT3 2019",
        "porsche_991ii_gt3_r": "Porsche 911 II GT3 R 2019",
        # GT4
        "alpine_a110_gt4": "Alpine A110 GT4 2018",
        "amr_v8_vantage_gt4": "Aston Martin Vantage AMR GT4 2018",
        "audi_r8_gt4": "Audi R8 LMS GT4 2016",
        "bmw_m4_gt4": "BMW M4 GT42 018",
        "chevrolet_camaro_gt4r": "Chevrolet Camaro GT4 R 2017",
        "ginetta_g55_gt4": "Ginetta G55 GT4 2012",
        "ktm_xbow_gt4": "Ktm Xbow GT4 2016",
        "maserati_mc_gt4": "Maserati Gran Turismo MC GT4 2016",
        "mclaren_570s_gt4": "McLaren 570s GT4 2016",
        "mercedes_amg_gt4": "Mercedes AMG GT4 2016",
        "porsche_718_cayman_gt4_mr": "Porsche 718 Cayman GT4 MR 2019",
        # GT3 - 2020
        "ferrari_488_gt3_evo": "Ferrari 488 GT3 Evo 2020",
        "mercedes_amg_gt3_evo": "Mercedes AMG GT3 Evo 2020",
        # GT3 - 2021
        "bmw_m4_gt3": "BMW M4 vGT3 2021",
        # Challengers Pack - 2022
        "audi_r8_lms_evo_ii": "Audi R8 LMS Evo II 2022",
        "bmw_m2_cs_racing": "BMW M2 Cup 2020",
        "ferrari_488_challenge_evo": "Ferrari 488 Challenge Evo 2020",
        "lamborghini_huracan_st_evo2": "Lamborghini Huracan ST Evo2 2021",
        "porsche_992_gt3_cup": "Porsche 992 GT3 Cup 2021"
    }
    return car[enum]


def track_name(enum):
    track = {
        "barcelona": "Barcelona",
        "brands_hatch": "Brands Hatch",
        "hungaroring": "Hungaroring",
        "kyalami": "Kyalami",
        "laguna_seca": "Laguna Seca",
        "misano": "Misano",
        "monza": "Monza",
        "mount_panorama": "Mount Panorama",
        "nurburgring": "Nurburgring",
        "paul_ricard": "Paul Ricard",
        "silverstone": "Silverstone",
        "spa": "Spa Francochamps",
        "suzuka": "Suzuka",
        "zolder": "Zolder",
        "zandvoort": "Zandvoort",
        "imola": "Imola",
        "oulton_park": "Oulton Park",
        "donington": "Donnington",
        "snetterton": "Snetterton",
        "cota": "Circuit of the Americas",
        "indianapolis": "Indianapolis",
        "watkins_glen": "Watkins Glen"
    }
    return track[enum]


def car_class(car):
    match car:
        case "porsche_992_gt3_cup", "porsche_991ii_gt3_cup":
            return "CUP"
        case "lamborghini_huracan_st_evo2", "lamborghini_huracan_st":
            return "ST"
        case "ferrari_488_challenge_evo":
            return "CHL"
        case "bmw_m2_cs_racing":
            return "TCX"
        case "alpine_a110_gt4", "amr_v8_vantage_gt4", "audi_r8_gt4", "bmw_m4_gt4", "chevrolet_camaro_gt4r", \
             "ginetta_g55_gt4", "ktm_xbow_gt4", "maserati_mc_gt4", "mclaren_570s_gt4", "mercedes_amg_gt4", \
             "porsche_718_cayman_gt4_mr":
            return "GT4"
        case _:
            return "GT3"
