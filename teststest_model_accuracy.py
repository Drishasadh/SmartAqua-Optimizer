# tests/test_model_accuracy.py
from services.data_generator import generate_historical_data
from services.model_service import train_model

def run_test_model():
    df = generate_historical_data(300)
    mae = train_model(df)
    assert mae < 35  # just a rough bound
    print(f"✅ test_model_accuracy: PASS (MAE={mae:.2f})")

if __name__ == "__main__":
    run_test_model()
