# main.py – FINAL FIXED VERSION

import time
import pandas as pd
from pathlib import Path

from data_generator import generate_historical_data, generate_realtime_sample
from model_trainer import train_ml_model
from water_optimizer import optimize_cooling
from db_service import DatabaseService
from visualizer import plot_all_graphs

DATASET_PATH = Path("data/dataset.csv")
OPT_DATASET_PATH = Path("data/optimized_dataset.csv")

def step1_create_dataset():
    if DATASET_PATH.exists():
        print("✔ Dataset already exists.")
        df = pd.read_csv(DATASET_PATH, parse_dates=["timestamp"])
    else:
        print("✔ Generating dataset...")
        df = generate_historical_data(n_rows=2000)
        DATASET_PATH.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(DATASET_PATH, index=False)
        print("✔ Dataset created.")
    return df

def step2_train_ml(df):
    print("✔ Training ML model...")
    model = train_ml_model(df)
    print("✔ Model training completed!")
    return model

def step3_run_realtime(model):
    print("✔ Running simulation...")
    db = DatabaseService()
    optimized_rows = []

    for cycle in range(10):
        sample = generate_realtime_sample()

        # EXACT 5 FEATURES
        X_input = [[
            sample["rack_load_kw"],
            sample["outside_temp_c"],
            sample["humidity_pct"],
            sample["inlet_temp_c"],
            sample["water_available_l"]
        ]]

        pred_kw = model.predict(X_input)[0]
        sample["required_cooling_kw"] = float(pred_kw)

        optimized = optimize_cooling(
            predicted_cooling_kw=sample["required_cooling_kw"],
            water_available_l=sample["water_available_l"]
        )

        row = {**sample, **optimized}
        optimized_rows.append(row)
        db.insert_log(row)

        print(f"→ Cycle {cycle+1} OK | Mode={optimized['mode']} | Used={optimized['water_used_l']} L")

        time.sleep(0.3)

    df_opt = pd.DataFrame(optimized_rows)
    df_opt.to_csv(OPT_DATASET_PATH, index=False)
    print("✔ Simulation completed.")
    return df_opt

def step4_graphs():
    print("✔ Creating graphs...")
    plot_all_graphs()
    print("✔ Graphs ready.")

if __name__ == "__main__":
    print("\n💧 AquaLess DC Enterprise – Starting...\n")
    df = step1_create_dataset()
    model = step2_train_ml(df)
    step3_run_realtime(model)
    step4_graphs()
    print("\n🎉 PROJECT COMPLETED SUCCESSFULLY!\n")



