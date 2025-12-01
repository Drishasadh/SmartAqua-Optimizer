# data_generator.py – FINAL VERSION

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random

def generate_historical_data(n_rows=2000):
    now = datetime.now()
    timestamps = [now - timedelta(minutes=5*i) for i in range(n_rows)]

    rack_load_kw = np.random.uniform(20, 250, size=n_rows)
    outside_temp = np.random.uniform(20, 45, size=n_rows)
    humidity = np.random.uniform(30, 80, size=n_rows)
    inlet_temp = 18 + (rack_load_kw/250)*10 + (outside_temp-25)*0.2

    required_cooling_kw = rack_load_kw*0.8 + np.maximum(0, inlet_temp-24)*1.5
    required_cooling_kw = np.clip(required_cooling_kw, 30, 450)

    water_available_l = np.random.uniform(500, 5000, size=n_rows)

    water_used_l = np.where(required_cooling_kw < 80, 5,
                    np.where(required_cooling_kw < 120, 25, 60))

    return pd.DataFrame({
        "timestamp": timestamps,
        "rack_load_kw": rack_load_kw,
        "outside_temp_c": outside_temp,
        "humidity_pct": humidity,
        "inlet_temp_c": inlet_temp,
        "water_available_l": water_available_l,
        "required_cooling_kw": required_cooling_kw,
        "water_used_l": water_used_l
    })


def generate_realtime_sample():
    return {
        "timestamp": datetime.now().isoformat(),
        "rack_load_kw": random.uniform(30, 260),
        "outside_temp_c": random.uniform(20, 45),
        "humidity_pct": random.uniform(30, 80),
        "inlet_temp_c": random.uniform(18, 30),
        "water_available_l": random.uniform(300, 5000)
    }


