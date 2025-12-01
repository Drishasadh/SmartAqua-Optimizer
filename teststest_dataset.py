# tests/test_dataset.py
import pandas as pd
from services.data_generator import generate_historical_data

def run_test_dataset():
    df = generate_historical_data(100)
    assert len(df) == 100
    needed_cols = [
        "rack_load_kw", "outside_temp_c", "humidity_pct",
        "inlet_temp_c", "water_available_l", "required_cooling_kw"
    ]
    for c in needed_cols:
        assert c in df.columns
    print("✅ test_dataset: PASS")

if __name__ == "__main__":
    run_test_dataset()
