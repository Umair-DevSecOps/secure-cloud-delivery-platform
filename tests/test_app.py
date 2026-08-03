from app import app


def test_health_endpoint():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200


def test_get_employees():
    client = app.test_client()

    response = client.get("/employees")

    assert response.status_code == 200

    data = response.get_json()

    assert len(data) == 2