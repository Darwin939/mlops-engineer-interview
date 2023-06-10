from fastapi.testclient import TestClient
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import main


client = TestClient(main.app)


def test_prediction():
    input_data = {
        "input_values": [-0.00551455, -0.04464164,  0.05630715, -0.03665608, -0.04835136,
                         -0.04296262, -0.07285395,  0.03799897,  0.05078203,  0.0569118]
    }
    response = client.post("/predict/", json=input_data)
    assert response.status_code == 200
    assert int(response.json().get('prediction')[0]) == 237
