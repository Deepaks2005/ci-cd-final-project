import os
import unittest

os.environ["DATABASE_URI"] = "sqlite:///:memory:"

from service import app, db


class RouteTestCase(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()
        with app.app_context():
            db.drop_all()
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_health(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "ok")

    def test_create_and_get_customer(self):
        response = self.client.post(
            "/customers", json={"name": "Deepak", "email": "deepak@example.com"}
        )
        self.assertEqual(response.status_code, 201)
        customer_id = response.get_json()["id"]

        response = self.client.get(f"/customers/{customer_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["name"], "Deepak")

    def test_invalid_customer(self):
        response = self.client.post("/customers", json={"name": "Deepak"})
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
