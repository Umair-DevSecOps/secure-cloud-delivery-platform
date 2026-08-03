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