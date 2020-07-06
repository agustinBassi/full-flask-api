import unittest
import os
import json

from ..app import create_app, db

class StateTest(unittest.TestCase):
    """
    states Test Case
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

    def test_get_all_states(self):
        res = self.client().get(
            '/api/v1/states/', 
            headers={'Content-Type': 'application/json'}, 
            )
        self.assertEqual(res.status_code, 200)

    def test_get_state_ok(self):
        # create the state and get its ID
        res = self.client().get(
            '/api/v1/states/1/', 
            headers={'Content-Type': 'application/json'}, 
            )
        json_data = json.loads(res.data)
        self.assertEqual(json_data['id'], 1)
        self.assertEqual(res.status_code, 200)

    def test_get_state_not_found(self):
        # request for this state
        res = self.client().get(
            f'/api/v1/states/999999/', 
            headers={'Content-Type': 'application/json'}, 
            )
        self.assertEqual(res.status_code, 404)

    def test_create_state_ok(self):
        # create a fake state
        state = {
            "name": "Nueva provinicia",
            "code": 100
        }
        # send request to create state
        res = self.client().post(
            '/api/v1/states/', 
            headers={'Content-Type': 'application/json'}, 
            data=json.dumps(state)
            )
        # get data from request
        json_data = json.loads(res.data)
        # assert received results
        self.assertEqual(json_data.get('name'), "Nueva provinicia")
        self.assertEqual(json_data.get('code'), 100)
        self.assertEqual(res.status_code, 201)

    def test_create_state_bad_request(self):
        # create a fake state
        states = [
            {},
            # state with no state
            {
            "name": "Provincia",
            },
            # state with no name
            {
            "code": 150,
            },
        ]
        for state in states:
            # send request to create state
            res = self.client().post(
                '/api/v1/states/', 
                headers={'Content-Type': 'application/json'}, 
                data=json.dumps(state)
                )
            self.assertEqual(res.status_code, 400)

    def test_update_state_ok(self):
        # create a fake state
        state = {
            "name": "Provincia",
            "code": 150
        }
        # create the state and get its ID
        res = self.client().post(
            '/api/v1/states/', 
            headers={'Content-Type': 'application/json'}, 
            data=json.dumps(state)
            )
        # check if state was correctly created
        self.assertEqual(res.status_code, 201)
        json_data = json.loads(res.data)
        state_id = 1#json_data['id']
        state_new_data = {
            "name": "Nueva Provincia",
            "code": 150
        }
        # request for this state
        res = self.client().put(
            f'/api/v1/states/{state_id}/', 
            headers={'Content-Type': 'application/json'}, 
            data=json.dumps(state_new_data)
            )
        json_data = json.loads(res.data)
    
    def test_update_state_not_found(self):
        state_new_data = {
            "name": "Nueva Provincia",
        }
        # request for this state
        res = self.client().put(
            f'/api/v1/states/999999/', 
            headers={'Content-Type': 'application/json'}, 
            data=json.dumps(state_new_data)
            )

        self.assertEqual(res.status_code, 404)

    def test_update_state_bad_request(self):
        # create a fake state
        state = {
            "name": "Nueva provinicia",
            "code": 100
        }
        # send request to create state
        res = self.client().post(
            '/api/v1/states/', 
            headers={'Content-Type': 'application/json'}, 
            data=json.dumps(state)
            )
        self.assertEqual(res.status_code, 201)
        json_data = json.loads(res.data)
        state_id = json_data['id']
        # create a fake state
        states = [
            {},
            # state with no state
            {
            "name": "Provincia",
            },
            # state with no name
            {
            "code": 150,
            },
        ]
        for state in states:
            # send request to create state
            res = self.client().put(
                f'/api/v1/states/{state_id}/', 
                headers={'Content-Type': 'application/json'}, 
                data=json.dumps(state)
                )
            self.assertEqual(res.status_code, 400)

    def test_delete_state_ok(self):
        # create a fake state
        state = {
            "name": "Nueva provinicia",
            "code": 100
        }
        # send request to create state
        res = self.client().post(
            '/api/v1/states/', 
            headers={'Content-Type': 'application/json'}, 
            data=json.dumps(state)
            )
        self.assertEqual(res.status_code, 201)
        json_data = json.loads(res.data)
        state_id = json_data['id']
        # request for this state
        res = self.client().delete(
            f'/api/v1/states/{state_id}/', 
            headers={'Content-Type': 'application/json'}, 
            )
        self.assertEqual(res.status_code, 204)

    def test_delete_state_not_found(self):
        # request for this state
        res = self.client().delete(
            f'/api/v1/states/999999/', 
            headers={'Content-Type': 'application/json'}, 
            )
        self.assertEqual(res.status_code, 404)


if __name__ == "__main__":
  unittest.main() 