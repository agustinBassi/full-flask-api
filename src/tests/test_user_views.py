import unittest
import os
import json

from ..app import create_app, db

class UsersTest(unittest.TestCase):
    """
    Users Test Case
    """
    def setUp(self):
        """
        Test Setup
        """
        self.app = create_app("testing")
        self.client = self.app.test_client
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """
        Tear Down
        """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_all_users(self):
        res = self.client().get(
            '/api/v1/users/', 
            headers={'Content-Type': 'application/json'}, 
            )
        self.assertEqual(res.status_code, 200)

    def test_get_user_ok(self):
        # create a fake user
        user = {
            "name": "Agustin",
            "age": 30,
            "state_code": 1
        }
        # create the user and get its ID
        res = self.client().post(
            '/api/v1/users/', 
            headers={'Content-Type': 'application/json'}, 
            data=json.dumps(user)
            )
        # check if user was correctly created
        self.assertEqual(res.status_code, 201)
        json_data = json.loads(res.data)
        user_id = json_data['id']
        # request for this user
        res = self.client().get(
            f'/api/v1/users/{user_id}/', 
            headers={'Content-Type': 'application/json'}, 
            )
        json_data = json.loads(res.data)
        self.assertEqual(json_data['id'], user_id)
        self.assertEqual(res.status_code, 200)

    def test_get_user_not_found(self):
        # request for this user
        res = self.client().get(
            f'/api/v1/users/999999/', 
            headers={'Content-Type': 'application/json'}, 
            )
        self.assertEqual(res.status_code, 404)

    def test_create_user_ok(self):
        # create a fake user
        user = {
            "name": "Agustin",
            "age": 30,
            "state_code": 1
        }
        # send request to create user
        res = self.client().post(
            '/api/v1/users/', 
            headers={'Content-Type': 'application/json'}, 
            data=json.dumps(user)
            )
        # get data from request
        json_data = json.loads(res.data)
        # assert received results
        self.assertEqual(json_data.get('name'), "Agustin")
        self.assertEqual(json_data.get('age'), 30)
        self.assertEqual(json_data.get('state').get('code'), 1)
        self.assertEqual(res.status_code, 201)

    def test_create_user_bad_request(self):
        # create a fake user
        users = [
            {},
            # user with no state
            {
            "name": "Agustin",
            "age": 30,
            },
            # user with no age
            {
            "name": "Agustin",
            "state_code": 1,
            },
            # user with no name
            {
            "age": 30,
            "state_code": 1,
            },
            # user with no invalid state_code
            {
            "name": "Agustin",
            "age": 30,
            "state_code": 999,
            }
        ]
        for user in users:
            # send request to create user
            res = self.client().post(
                '/api/v1/users/', 
                headers={'Content-Type': 'application/json'}, 
                data=json.dumps(user)
                )
            self.assertEqual(res.status_code, 400)

    def test_update_user_ok(self):
        # create a fake user
        user = {
            "name": "Agustin",
            "age": 30,
            "state_code": 1
        }
        # create the user and get its ID
        res = self.client().post(
            '/api/v1/users/', 
            headers={'Content-Type': 'application/json'}, 
            data=json.dumps(user)
            )
        # check if user was correctly created
        self.assertEqual(res.status_code, 201)
        json_data = json.loads(res.data)
        user_id = json_data['id']
        user_new_data = {
            "name": "Agustin Bassi",
            "age": 31,
            "state_code": 2
        }
        # request for this user
        res = self.client().put(
            f'/api/v1/users/{user_id}/', 
            headers={'Content-Type': 'application/json'}, 
            data=json.dumps(user_new_data)
            )
        json_data = json.loads(res.data)
        self.assertEqual(json_data['id'], user_id)
        self.assertEqual(json_data['name'], "Agustin Bassi")
        self.assertEqual(json_data['age'], 31)
        self.assertEqual(res.status_code, 200)
    
    def test_update_user_not_found(self):
        user_new_data = {
            "name": "Agustin Bassi",
            "age": 31,
            "state_code": 2
        }
        # request for this user
        res = self.client().put(
            f'/api/v1/users/999999/', 
            headers={'Content-Type': 'application/json'}, 
            data=json.dumps(user_new_data)
            )

        self.assertEqual(res.status_code, 404)

    def test_update_user_bad_request(self):
        # create a fake user
        user = {
            "name": "Agustin",
            "age": 30,
            "state_code": 1
        }
        # create the user and get its ID
        res = self.client().post(
            '/api/v1/users/', 
            headers={'Content-Type': 'application/json'}, 
            data=json.dumps(user)
            )
        # check if user was correctly created
        self.assertEqual(res.status_code, 201)
        json_data = json.loads(res.data)
        user_id = json_data['id']
        # create a fake user
        users = [
            {},
            # user with no state
            {
            "name": "Agustin",
            "age": 30,
            },
            # user with no age
            {
            "name": "Agustin",
            "state_code": 1,
            },
            # user with no name
            {
            "age": 30,
            "state_code": 1,
            },
            # user with no invalid state_code
            {
            "name": "Agustin",
            "age": 30,
            "state_code": 999,
            }
        ]
        for user in users:
            # send request to create user
            res = self.client().put(
                f'/api/v1/users/{user_id}/', 
                headers={'Content-Type': 'application/json'}, 
                data=json.dumps(user)
                )
            self.assertEqual(res.status_code, 400)

    def test_delete_user_ok(self):
        # create a fake user
        user = {
            "name": "Agustin",
            "age": 30,
            "state_code": 1
        }
        # create the user and get its ID
        res = self.client().post(
            '/api/v1/users/', 
            headers={'Content-Type': 'application/json'}, 
            data=json.dumps(user)
            )
        # check if user was correctly created
        self.assertEqual(res.status_code, 201)
        json_data = json.loads(res.data)
        user_id = json_data['id']
        # request for this user
        res = self.client().delete(
            f'/api/v1/users/{user_id}/', 
            headers={'Content-Type': 'application/json'}, 
            )
        self.assertEqual(res.status_code, 204)

    def test_delete_user_not_found(self):
        # request for this user
        res = self.client().delete(
            f'/api/v1/users/999999/', 
            headers={'Content-Type': 'application/json'}, 
            )
        self.assertEqual(res.status_code, 404)


if __name__ == "__main__":
  unittest.main() 