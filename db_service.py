
# db_service.py – FINAL VERSION

import sqlite3
from pathlib import Path

class DatabaseService:
    def __init__(self):
        self.db_path = Path("data/aqualess_logs.db")
        self.db_path.parent.mkdir(exist_ok=True)
        self.conn = sqlite3.connect(self.db_path)
        self._create()

    def _create(self):
        q = """
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            rack_load_kw REAL,
            outside_temp_c REAL,
            humidity_pct REAL,
            inlet_temp_c REAL,
            water_available_l REAL,
            required_cooling_kw REAL,
            mode TEXT,
            water_used_l REAL,
            water_saved_l REAL
        );
        """
        self.conn.execute(q)
        self.conn.commit()

    def insert_log(self, row):
        q = """
        INSERT INTO logs (
            timestamp, rack_load_kw, outside_temp_c, humidity_pct,
            inlet_temp_c, water_available_l, required_cooling_kw,
            mode, water_used_l, water_saved_l
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        values = (
            row["timestamp"],
            row["rack_load_kw"],
            row["outside_temp_c"],
            row["humidity_pct"],
            row["inlet_temp_c"],
            row["water_available_l"],
            row["required_cooling_kw"],
            row["mode"],
            row["water_used_l"],
            row["water_saved_l"]
        )
        self.conn.execute(q, values)
        self.conn.commit()


def fetch_last_n(conn, n=50):
    q = "SELECT * FROM logs ORDER BY id DESC LIMIT ?"
    return conn.execute(q, (n,)).fetchall()
