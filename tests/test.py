from flask import Flask, json

import unittest

app = Flask(__name__)


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.test_client = app.test_client()
    
        self.request_data = {
            "iD":1,
            "fullname":"naz",
            "Computer-ID":"AAAywths",
            "description":"Screen",
            "department":"HR"
        }

    
    def tearDown(self):
        requests = []
        

class RequestTestCase(BaseTestCase):

    def test_create_request(self):
        response = self.test_client.post(
            '/API/v1/users/requests', data=json.dumps(self.request_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn(
            "You have created a request", str(response.data))

    def test_create_request_with_missing_credentials(self):
       
        response = self.test_client.post('/API/v1/users/requests', data=json.dumps({"fullname": "naz", "Computer-ID":"AAAywths", "description":"Screen","department": ""}), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_create_request_without_client_name(self):
        """ Test for create request without client name """
        with self.test_client:
            response = self.test_client.post('/API/v1/users/requests', content_type='application/json',
                                             data=json.dumps({"Computer-ID":"AAAywths", "description":"Screen","department":"HR"}))
            reply = json.loads(response.data)
            self.assertEqual(reply["message"], "client name is required")
            self.assertEqual(response.status_code, 400)

    def test_get_all_requests(self):
        """ Tests whether a user can fetch all his/her requests successfully """


        response = self.test_client.post(
            '/API/v1/users/requests', data=json.dumps(self.request_data), content_type='application/json')
        response = self.test_client.get(
            '/API/v1/users/requests', data=json.dumps(self.request_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)


    def test_get_single_request(self):
        """ Tests  whether a single request can be returned by id successfully """
        response = self.test_client.get(
            '/API/v1/users/requests', data=json.dumps(self.request_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)


    def test_request_with_missing_credentials(self):
        """Tests user can\'t send request with missing details"""
        response = self.test_client.post('/API/v1/users/requests', data=json.dumps({ "fullname": "naz", "description":"Screen","department": ""}), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_create_request_with_invalid_email(self):
        response = self.test_client.post('/API/v1/users/requests', data=json.dumps({ "fullname": "naz", "Computer-ID":"AAAywths", "description":"Screen","department":  ""}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Enter a valid email', str(response.data))    
        
if __name__ == "__main__":
    unittest.main()
