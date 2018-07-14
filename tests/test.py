from flask import Flask
import unittest, json
from .data import BaseTestCase


class RequestTestCase(BaseTestCase):
    
    def test_create_request(self):
    
        response = self.test_client.post('/nazirini/api/v1.0/details', data=json.dumps(self.request), content_type = 'application/json')
        self.assertEqual(response.status_code, 404)
       

    def test_modify_request(self):
    
        response = self.test_client.put('/nazirini/api/v1.0/details/1', data=json.dumps(self.request), content_type = 'application/json')
        self.assertEqual(response.status_code, 404)
         

    def test_get_all_requests(self):
       
        response = self.test_client.post('/nazirini/api/v1.0/details', data=json.dumps(self.request), content_type = 'application/json')
        response = self.test_client.get('/nazirini/api/v1.0/details', data=json.dumps(self.request), content_type = 'application/json')
        self.assertEqual(response.status_code, 404)
          
    def test_get_single_request(self):
       
        response = self.test_client.get('/nazirini/api/v1.0/details/1', data=json.dumps(self.request), content_type = 'application/json')
        self.assertEqual(response.status_code, 404)

    def test_cant_create_a_user(self):
        invalid_user = json.dumps({"fuulname":"nazirini", "email":"hansu@gmail.com", "phone":"536780","department":"Team Lead","computerID":"AAA53","description":"screen freezes when handling heavy apps"})
        response = self.test_client.post('/nazirini/api/v1.0/details', data=invalid_user, content_type=self.content_type)
        self.assertTrue(response.status_code == 404)

                
    if __name__ == '__main__':
        unittest.main()