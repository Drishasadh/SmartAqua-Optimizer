def optimize_cooling(predicted_cooling_kw: float,
                     water_available_l: float) -> dict:

    water_needed = max(0.0, (predicted_cooling_kw - 60) * 4)

    if water_available_l < 1000 and water_needed > water_available_l * 0.6:
        return {
            "mode": "air",
            "water_used_l": 0.0,
            "water_saved_l": water_needed
        }

    return {
        "mode": "water",
        "water_used_l": min(water_needed, water_available_l),
        "water_saved_l": 0.0
    }
