from flask import request
from app import app
from app.data import employees



@app.route("/")
def home():
    return {
        "message": "Secure Cloud Delivery Platform API"
    }


@app.route("/health")
def health():
    return {
        "status": "healthy"
    }, 200


@app.route("/employees")
def get_employees():
    return employees, 200

@app.route("/employees/<int:employee_id>")
def get_employee(employee_id):

    for employee in employees:
        if employee["id"] == employee_id:
            return employee, 200

    return {
        "error": "Employee not found"
    }, 404

@app.route("/employees", methods=["POST"])


def create_employee():

    data = request.get_json()

    new_employee = {
        "id": len(employees) + 1,
        "name": data["name"],
        "email": data["email"],
        "department": data["department"],
        "role": data["role"]
    }

    employees.append(new_employee)

    return new_employee, 201

@app.route("/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):

    data = request.get_json()

    for employee in employees:

        if employee["id"] == employee_id:

            employee["name"] = data.get(
                "name",
                employee["name"]
            )

            employee["email"] = data.get(
                "email",
                employee["email"]
            )

            employee["department"] = data.get(
                "department",
                employee["department"]
            )

            employee["role"] = data.get(
                "role",
                employee["role"]
            )

            return employee, 200

    return {
        "error": "Employee not found"
    }, 404