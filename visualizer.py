# visualizer.py – FINAL VERSION (Drisha Edition)

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from db_service import fetch_last_n   # ✔ fixed import


DB_PATH = Path("data/aqualess_logs.db")


def plot_all_graphs():
    """Load recent data from SQLite and generate graphs."""

    conn = None
    try:
        import sqlite3
        conn = sqlite3.connect(DB_PATH)

        rows = fetch_last_n(conn, n=50)
        if not rows:
            print("⚠ No log data found in DB. Run simulation first.")
            return

        # Convert to dataframe
        df = pd.DataFrame(rows, columns=[
            "id", "timestamp", "rack_load_kw", "outside_temp_c",
            "humidity_pct", "inlet_temp_c", "water_available_l",
            "required_cooling_kw", "mode", "water_used_l", "water_saved_l"
        ])

        # Convert timestamp to datetime
        df["timestamp"] = pd.to_datetime(df["timestamp"])

        # Create output folder
        out_dir = Path("graphs")
        out_dir.mkdir(exist_ok=True)

        # -------- Graph 1: Rack load --------
        plt.figure(figsize=(10, 5))
        plt.plot(df["timestamp"], df["rack_load_kw"], marker="o")
        plt.title("Rack Load (kW)")
        plt.xlabel("Time")
        plt.ylabel("kW")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(out_dir / "rack_load.png")
        plt.close()

        # -------- Graph 2: Required cooling --------
        plt.figure(figsize=(10, 5))
        plt.plot(df["timestamp"], df["required_cooling_kw"], color="red", marker="o")
        plt.title("Required Cooling (kW)")
        plt.xlabel("Time")
        plt.ylabel("Cooling kW")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(out_dir / "required_cooling.png")
        plt.close()

        # -------- Graph 3: Water Used --------
        plt.figure(figsize=(10, 5))
        plt.plot(df["timestamp"], df["water_used_l"], color="blue", marker="o")
        plt.title("Water Used (L)")
        plt.xlabel("Time")
        plt.ylabel("Liters")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(out_dir / "water_used.png")
        plt.close()

        # -------- Graph 4: Water Saved --------
        plt.figure(figsize=(10, 5))
        plt.plot(df["timestamp"], df["water_saved_l"], color="green", marker="o")
        plt.title("Water Saved (L)")
        plt.xlabel("Time")
        plt.ylabel("Liters Saved")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(out_dir / "water_saved.png")
        plt.close()

        print("📊 Graphs created successfully in /graphs folder!")

    except Exception as e:
        print("❌ Error while plotting graphs:", e)

    finally:
        if conn:
            conn.close()


