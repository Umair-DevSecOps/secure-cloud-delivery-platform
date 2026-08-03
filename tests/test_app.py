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


def test_get_employee_by_id():
    client = app.test_client()

    response = client.get("/employees/1")

    assert response.status_code == 200

    data = response.get_json()

    assert data["id"] == 1
    assert data["name"] == "Alice Smith"


def test_create_employee():
    client = app.test_client()

    new_employee = {
        "name": "Charlie Brown",
        "email": "charlie@company.com",
        "department": "Security",
        "role": "Engineer"
    }

    response = client.post("/employees", json=new_employee)

    assert response.status_code == 201

    data = response.get_json()

    assert data["name"] == "Charlie Brown"
    assert data["email"] == "charlie@company.com"