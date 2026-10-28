from flask import Blueprint, jsonify, request
from service import db
from service.models import Customer

api = Blueprint("api", __name__)


@api.get("/")
def health():
    return jsonify({"status": "ok", "service": "devops-capstone"})


@api.get("/customers")
def list_customers():
    return jsonify([customer.to_dict() for customer in Customer.query.all()])


@api.post("/customers")
def create_customer():
    data = request.get_json(silent=True) or {}
    name = data.get("name")
    email = data.get("email")
    if not name or not email:
        return jsonify({"error": "name and email are required"}), 400
    if Customer.query.filter_by(email=email).first():
        return jsonify({"error": "email already exists"}), 409
    customer = Customer(name=name, email=email)
    db.session.add(customer)
    db.session.commit()
    return jsonify(customer.to_dict()), 201


@api.get("/customers/<int:customer_id>")
def get_customer(customer_id):
    customer = db.session.get(Customer, customer_id)
    if not customer:
        return jsonify({"error": "customer not found"}), 404
    return jsonify(customer.to_dict())


@api.delete("/customers/<int:customer_id>")
def delete_customer(customer_id):
    customer = db.session.get(Customer, customer_id)
    if not customer:
        return jsonify({"error": "customer not found"}), 404
    db.session.delete(customer)
    db.session.commit()
    return "", 204
