from flask import Flask
import unittest 

app = Flask(__name__)

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.request = {
        'fullname': 'nazirini ',
        'email': 'hansu@gmail.com',
        'phone': '536780',
        'department': 'Team Lead',
        'computerID': 'AAA53',
        'description': 'Screen freezes when handling heavy apps'}
        self.content_type = "application/json"
        self.test_client = app.test_client()

    def tearDown(self):
        pass