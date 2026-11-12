import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))
from app import app

def test_health():
    r = app.test_client().get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "healthy"

def test_menu():
    r = app.test_client().get("/api/menu")
    assert r.status_code == 200 and len(r.get_json()) == 3

def test_valid_order():
    assert app.test_client().post("/api/orders", json={"item_id": 1}).status_code == 201

def test_invalid_order():
    assert app.test_client().post("/api/orders", json={"item_id": 999}).status_code == 400
