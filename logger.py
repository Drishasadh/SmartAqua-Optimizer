# logger.py

import sqlite3
from datetime import datetime

DB_NAME = "aqualess_logs.db"

class ExperimentLogger:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.create_table()

    def create_table(self):
        q = """
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            rack_load_kw REAL,
            outside_temp REAL,
            humidity REAL,
            inlet_temp REAL,
            water_available_l REAL,
            required_cooling_kw REAL,
            water_used_l REAL,
            water_saved_l REAL
        )
        """
        self.conn.execute(q)
        self.conn.commit()

    def log(self, row: dict):
        q = """
        INSERT INTO logs (timestamp, rack_load_kw, outside_temp, humidity,
                          inlet_temp, water_available_l, required_cooling_kw,
                          water_used_l, water_saved_l)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.conn.execute(q, (
            row["timestamp"],
            row["rack_load_kw"],
            row["outside_temp"],
            row["humidity"],
            row["inlet_temp"],
            row["water_available_l"],
            row["required_cooling_kw"],
            row["water_used_l"],
            row["water_saved_l"]
        ))
        self.conn.commit()

