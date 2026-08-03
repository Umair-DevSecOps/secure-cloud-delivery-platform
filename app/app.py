from flask import Flask
from app.data import employees

app = Flask(__name__)


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

if __name__ == "__main__":
    app.run(debug=True)