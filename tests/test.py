from flask import Flask
import json 


import unittest


app = Flask(__name__)

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.user = {
        'fullname': 'nazirini ',
        'email': 'hansu@gmail.com',
        'phone': '536780',
        'department': 'Team Lead',
        'computerID': 'AAA53',
        'description': 'Screen freezes when handing heavy apps'}
        self.content_type = "application/json"
        self.test_client = app.test_client()

    def tearDown(self):
        pass




class ApiTestcase(BaseTestCase):
    
    
    def test_can_fetch_users(self):
        response = self.test_client.get('/nazirini/api/v1.0/details')
        self.assertEqual(response.status_code, 200 )
        self.assertIn("users", response.data.decode())
    

    def test_can_create_user(self):
        user_data = json.dumps(self.user)
        response = self.test_client.post('/nazirini/api/v1.0/details', data=user_data, content_type=self.content_type)
        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.data.decode())
        self.assertEqual(self.user, response_data.get('user'))

    if __name__ == '__main__':
        unittest.main()
