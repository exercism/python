import unittest

from rest_api import RestAPI

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.1
import json


class RestApiTest(unittest.TestCase):
    def test_no_users(self):
        database = {"users": []}
        api = RestAPI(database)

        response = api.get("/users")
        expected = {"users": []}
        self.assertDictEqual(json.loads(response), expected)

    def test_add_user(self):
        database = {"users": []}
        api = RestAPI(database)
        payload = json.dumps({"user": "Adam"})
        response = api.post("/add", payload)
        expected = {"name": "Adam", "owes": {}, "owed_by": {}, "balance": 0.0}
        self.assertDictEqual(json.loads(response), expected)

    def test_get_single_user(self):
        database = {
            "users": [
                {"name": "Adam", "owes": {}, "owed_by": {}, "balance": 0.0},
                {"name": "Bob", "owes": {}, "owed_by": {}, "balance": 0.0},
            ]
        }
        api = RestAPI(database)
        payload = json.dumps({"users": ["Bob"]})
        response = api.get("/users", payload)
        expected = {
            "users": [{"name": "Bob", "owes": {}, "owed_by": {}, "balance": 0.0}]
        }
        self.assertDictEqual(json.loads(response), expected)

    def test_both_users_have_0_balance(self):
        database = {
            "users": [
                {"name": "Adam", "owes": {}, "owed_by": {}, "balance": 0.0},
                {"name": "Bob", "owes": {}, "owed_by": {}, "balance": 0.0},
            ]
        }
        api = RestAPI(database)
        payload = json.dumps({"lender": "Adam", "borrower": "Bob", "amount": 3.0})
        response = api.post("/iou", payload)
        expected = {
            "users": [
                {"name": "Adam", "owes": {}, "owed_by": {"Bob": 3.0}, "balance": 3.0},
                {"name": "Bob", "owes": {"Adam": 3.0}, "owed_by": {}, "balance": -3.0},
            ]
        }
        self.assertDictEqual(json.loads(response), expected)

    def test_borrower_has_negative_balance(self):
        database = {
            "users": [
                {"name": "Adam", "owes": {}, "owed_by": {}, "balance": 0.0},
                {"name": "Bob", "owes": {"Chuck": 3.0}, "owed_by": {}, "balance": -3.0},
                {"name": "Chuck", "owes": {}, "owed_by": {"Bob": 3.0}, "balance": 3.0},
            ]
        }
        api = RestAPI(database)
        payload = json.dumps({"lender": "Adam", "borrower": "Bob", "amount": 3.0})
        response = api.post("/iou", payload)
        expected = {
            "users": [
                {"name": "Adam", "owes": {}, "owed_by": {"Bob": 3.0}, "balance": 3.0},
                {
                    "name": "Bob",
                    "owes": {"Adam": 3.0, "Chuck": 3.0},
                    "owed_by": {},
                    "balance": -6.0,
                },
            ]
        }
        self.assertDictEqual(json.loads(response), expected)

    def test_lender_has_negative_balance(self):
        database = {
            "users": [
                {"name": "Adam", "owes": {}, "owed_by": {}, "balance": 0.0},
                {"name": "Bob", "owes": {"Chuck": 3.0}, "owed_by": {}, "balance": -3.0},
                {"name": "Chuck", "owes": {}, "owed_by": {"Bob": 3.0}, "balance": 3.0},
            ]
        }
        api = RestAPI(database)
        payload = json.dumps({"lender": "Bob", "borrower": "Adam", "amount": 3.0})
        response = api.post("/iou", payload)
        expected = {
            "users": [
                {"name": "Adam", "owes": {"Bob": 3.0}, "owed_by": {}, "balance": -3.0},
                {
                    "name": "Bob",
                    "owes": {"Chuck": 3.0},
                    "owed_by": {"Adam": 3.0},
                    "balance": 0.0,
                },
            ]
        }
        self.assertDictEqual(json.loads(response), expected)

    def test_lender_owes_borrower(self):
        database = {
            "users": [
                {"name": "Adam", "owes": {"Bob": 3.0}, "owed_by": {}, "balance": -3.0},
                {"name": "Bob", "owes": {}, "owed_by": {"Adam": 3.0}, "balance": 3.0},
            ]
        }
        api = RestAPI(database)
        payload = json.dumps({"lender": "Adam", "borrower": "Bob", "amount": 2.0})
        response = api.post("/iou", payload)
        expected = {
            "users": [
                {"name": "Adam", "owes": {"Bob": 1.0}, "owed_by": {}, "balance": -1.0},
                {"name": "Bob", "owes": {}, "owed_by": {"Adam": 1.0}, "balance": 1.0},
            ]
        }
        self.assertDictEqual(json.loads(response), expected)

    def test_lender_owes_borrower_less_than_new_loan(self):
        database = {
            "users": [
                {"name": "Adam", "owes": {"Bob": 3.0}, "owed_by": {}, "balance": -3.0},
                {"name": "Bob", "owes": {}, "owed_by": {"Adam": 3.0}, "balance": 3.0},
            ]
        }
        api = RestAPI(database)
        payload = json.dumps({"lender": "Adam", "borrower": "Bob", "amount": 4.0})
        response = api.post("/iou", payload)
        expected = {
            "users": [
                {"name": "Adam", "owes": {}, "owed_by": {"Bob": 1.0}, "balance": 1.0},
                {"name": "Bob", "owes": {"Adam": 1.0}, "owed_by": {}, "balance": -1.0},
            ]
        }
        self.assertDictEqual(json.loads(response), expected)

    def test_lender_owes_borrower_same_as_new_loan(self):
        database = {
            "users": [
                {"name": "Adam", "owes": {"Bob": 3.0}, "owed_by": {}, "balance": -3.0},
                {"name": "Bob", "owes": {}, "owed_by": {"Adam": 3.0}, "balance": 3.0},
            ]
        }
        api = RestAPI(database)
        payload = json.dumps({"lender": "Adam", "borrower": "Bob", "amount": 3.0})
        response = api.post("/iou", payload)
        expected = {
            "users": [
                {"name": "Adam", "owes": {}, "owed_by": {}, "balance": 0.0},
                {"name": "Bob", "owes": {}, "owed_by": {}, "balance": 0.0},
            ]
        }
        self.assertDictEqual(json.loads(response), expected)


if __name__ == "__main__":
    unittest.main()
