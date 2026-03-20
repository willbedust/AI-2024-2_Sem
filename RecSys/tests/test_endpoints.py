from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def get_auth_headers():
    return {"Authorization": "Bearer testtoken"}


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data


def test_reco_success():
    response = client.get("/reco/dummy/973171", headers=get_auth_headers())
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == 973171
    assert "items" in data
    assert len(data["items"]) == 10


def test_reco_missing_token():
    response = client.get("/reco/dummy/973171")
    assert response.status_code in (401, 403)


def test_reco_invalid_token():
    response = client.get("/reco/dummy/973171", headers={"Authorization": "Bearer wrongtoken"})
    assert response.status_code == 401


def test_reco_invalid_model():
    response = client.get("/reco/unknown/973171", headers=get_auth_headers())
    assert response.status_code == 404
