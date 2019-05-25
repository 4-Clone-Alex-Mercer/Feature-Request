import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import unittest
from app.models import Client, ProductArea, FeatureRequest
from app import create_app, db
from flask_testing import TestCase
from flask import json
from datetime import datetime
from config import TestConfig



class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        return create_app(TestConfig)

    def setUp(self):
        db.create_all()
        db.session.add(Client(name='Client A'))
        db.session.add(Client(name='Client B'))
        db.session.add(Client(name='Client C'))
        db.session.add(ProductArea(name='Policies'))
        db.session.add(ProductArea(name='Billings'))
        db.session.add(ProductArea(name='Claims'))
        db.session.add(ProductArea(name='Reports'))
        featureRequest = FeatureRequest(
            title='First Title',
            description='First Description',
            target_date=datetime.strptime('2019/05/24', '%Y/%m/%d'),
            client_priority=1,
            client_id=3,
            product_area_id=2
        )
        db.session.add(featureRequest)
        featureRequest = FeatureRequest(
            title='Second Title',
            description='Second Description',
            target_date=datetime.strptime('2019/05/31', '%Y/%m/%d'),
            client_priority=1,
            client_id=2,
            product_area_id=3

        )
        db.session.add(featureRequest)
        featureRequest = FeatureRequest(
            title='Third Title',
            description='Third Description',
            target_date=datetime.strptime('2019/06/15', '%Y/%m/%d'),
            client_priority=1,
            client_id=1,
            product_area_id=1

        )
        db.session.add(featureRequest)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class FeatureRequestsTestCase(BaseTestCase):

    def test_main_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/html', str(response.headers))


    def test_get_feature_requests(self):
        response = self.client.get("/requests")
        contents = ['First Title', 'First Description',
                    'Billings', '1', 'Client A']
        for content in contents:
            self.assertIn(content, str(response.data))

    def test_create_feature_request(self):

        data = {'title': 'Title', 'description': 'Description',
                'target_date': '2019-1-7', 'client_priority': 1, 'client': 'Client A', 'product_area': 'Claims'}

        response = self.client.post(
            '/request/create',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(data),
        )
        self.assertEqual(200, response.status_code)

    def test_update_feature_request(self):

        data = {'title': 'Title', 'description': 'Description',
                'target_date': '2019-1-7', 'client_priority': 3, 'client': 'Client C', 'product_area': 'Claims', 'requestId': 1}

        response = self.client.put(
            '/request/update',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(data),
        )
        self.assertEqual(200, response.status_code)

    def test_delete_feature_request(self):

        data = "2"

        response = self.client.delete(
            '/request/delete',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(data),
        )
        self.assertEqual(200, response.status_code)

    def test_update_praiority(self):
        data = {'title': 'Title', 'description': 'Description',
                'target_date': '2019-1-7', 'client_priority': 1, 'client': 'Client A', 'product_area': 'Claims'}

        response = self.client.post(
            '/request/create',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(data),
        )
        response = self.client.get("/requests")
        priority = json.loads(response.data.decode(
            'utf-8'))[2]['client_priority']
        self.assertEqual(2, priority)


if __name__ == '__main__':
    unittest.main()
