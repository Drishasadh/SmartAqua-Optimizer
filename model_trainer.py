# model_trainer.py – FINAL FIXED VERSION

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


def train_ml_model(df: pd.DataFrame):
    """
    Train ML model to predict required_cooling_kw.
    """

    FEATURES = [
        "rack_load_kw",
        "outside_temp_c",
        "humidity_pct",
        "inlet_temp_c",
        "water_available_l"
    ]

    TARGET = "required_cooling_kw"

    X = df[FEATURES]
    y = df[TARGET]

    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )

    model.fit(X, y)
    return model
