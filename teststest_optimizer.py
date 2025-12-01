# tests/test_optimizer.py
from services.optimizer_service import optimize_cooling

def run_test_optimizer():
    # lots of water
    res1 = optimize_cooling(200, 4000)
    assert res1["mode"] == "water"

    # very low water
    res2 = optimize_cooling(250, 500)
    assert res2["mode"] == "air"
    print("✅ test_optimizer: PASS")

if __name__ == "__main__":
    run_test_optimizer()
