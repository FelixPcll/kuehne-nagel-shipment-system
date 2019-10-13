import json

from django.test import TestCase, Client
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Shipment
from ..serializer import ShipmentSerializer


# initialize the APIClient app
client = Client()

class CreateTestCase(APITestCase):

    def test_create_acept_full(self):
        pkg_data = {
            "track_ref": "AA123456789BR",
            "from_coutry": "Brazil",
            "to_country": "Estonia",
            "package_weight": 73.0,
            "is_up_to_date": True
        }

        response = self.client.post('/api/v0.1/shipment/', pkg_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_acept_missing_up_to_date(self):
        pkg_data = {
            "track_ref": "BR123456789ES",
            "from_coutry": "Brazil",
            "to_country": "Estonia",
            "package_weight": 73.0
        }

        response = self.client.post('/api/v0.1/shipment/', pkg_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["is_up_to_date"], True)

    def test_create_fail_missing_track_ref(self):
        pkg_data = {
            "from_coutry": "Brazil",
            "to_country": "Estonia",
            "package_weight": 73.0,
            "is_up_to_date": True
        }

        response = self.client.post('/api/v0.1/shipment/', pkg_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_fail_missing_from_coutry(self):
        pkg_data = {
            "track_ref": "AA123456789BR",
            "to_country": "Estonia",
            "package_weight": 73.0,
            "is_up_to_date": True
        }

        response = self.client.post('/api/v0.1/shipment/', pkg_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_fail_missing_to_country(self):
        pkg_data = {
            "track_ref": "AA123456789BR",
            "from_coutry": "Brazil",
            "package_weight": 73.0,
            "is_up_to_date": True
        }

        response = self.client.post('/api/v0.1/shipment/', pkg_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_fail_missing_package_weight(self):
        pkg_data = {
            "track_ref": "AA123456789BR",
            "from_coutry": "Brazil",
            "to_country": "Estonia",
            "is_up_to_date": True
        }

        response = self.client.post('/api/v0.1/shipment/', pkg_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RetrieveTestCase(APITestCase):

    def setUp(self):
        pkg_data = pkg_data = {
            "track_ref": "AA123456789BR",
            "from_coutry": "Brazil",
            "to_country": "Estonia",
            "package_weight": 73.0,
            # "is_up_to_date": True
        }

        post_response = self.client.post('/api/v0.1/shipment/', pkg_data)

    def test_retrive_acept_all(self):
        response = self.client.get('/api/v0.1/shipment/{}/'.format('AA123456789BR'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(len(response.data), 1)

        self.assertEqual(response.data["track_ref"], "AA123456789BR")
        self.assertEqual(response.data["from_coutry"], "Brazil")
        self.assertEqual(response.data["to_country"], "Estonia")
        self.assertEqual(response.data["package_weight"], 73.0)
        self.assertEqual(response.data["is_up_to_date"], True)


class UpdateTestCase(APITestCase):

    def setUp(self):
        pkg_data = {
            "track_ref": "AA123456789BR",
            "from_coutry": "Brazil",
            "to_country": "Estonia",
            "package_weight": 73.0,
            # "is_up_to_date": True
        }

        post_response = self.client.post('/api/v0.1/shipment/', pkg_data)

    def test_update_from_coutry(self):
        url = '/api/v0.1/shipment/{}/'.format('AA123456789BR')
        data = {
            "track_ref": "AA123456789BR",
            "from_coutry": "Spain",
            "to_country": "Estonia",
            "package_weight": 73.0,
        }

        response_put = self.client.put(url, data)
        self.assertEqual(response_put.status_code, status.HTTP_200_OK)

        response_get = self.client.get(url)
        self.assertEqual(response_get.data["from_coutry"], "Spain")

    def test_update_to_country(self):
        url = '/api/v0.1/shipment/{}/'.format('AA123456789BR')
        data = {
            "track_ref": "AA123456789BR",
            "from_coutry": "Brazil",
            "to_country": "Latvia",
            "package_weight": 73.0,
        }

        response_put = self.client.put(url, data)
        self.assertEqual(response_put.status_code, status.HTTP_200_OK)

        response_get = self.client.get(url)
        self.assertEqual(response_get.data["to_country"], "Latvia")

    def test_update_package_weight(self):
        url = '/api/v0.1/shipment/{}/'.format('AA123456789BR')
        data = {
            "track_ref": "AA123456789BR",
            "from_coutry": "Brazil",
            "to_country": "Estonia",
            "package_weight": 12,
        }

        response_put = self.client.put(url, data)
        self.assertEqual(response_put.status_code, status.HTTP_200_OK)

        response_get = self.client.get(url)
        self.assertEqual(response_get.data["package_weight"], 12)


class ListTestCase(APITestCase):
    def test_list_all(self):
        data = [
            {
                "track_ref": "AA123456789BR",
                "from_coutry": "Brazil",
                "to_country": "Estonia",
                "package_weight": 73.0,
                "is_up_to_date": True
            },
            {
                "track_ref": "AA987654321BR",
                "from_coutry": "United States of America",
                "to_country": "Chile",
                "package_weight": 1.085,
                "is_up_to_date": True
            },
            {
                "track_ref": "AA100833276BR",
                "from_coutry": "German",
                "to_country": "Japan",
                "package_weight": 0.6,
                "is_up_to_date": True
            }
        ]

        urls = []
        responses = []
        for item in data:
            urls.append('/api/v0.1/shipment/{}/'.format(item["track_ref"]))
            responses.append(self.client.post('/api/v0.1/shipment/', item))
        
        for response in responses:
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        response_list = self.client.get('/api/v0.1/shipment/')
        self.assertEqual(len(response_list.data), len(data))


class DeleteTestCase(APITestCase):
    def setUp(self):
        data = {
            "track_ref": "AA123456789BR",
            "from_coutry": "Brazil",
            "to_country": "Estonia",
            "package_weight": 73.0,
            "is_up_to_date": True
        }

        url_g = '/api/v0.1/shipment/'
        response_post = self.client.post(url_g, data)
        self.assertEqual(response_post.status_code, status.HTTP_201_CREATED)


    def test_delete_item(self):
        url_p = '/api/v0.1/shipment/{}/'.format("AA123456789BR")

        response_get = self.client.get(url_p)
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)

        response_del = self.client.delete(url_p)
        self.assertEqual(response_del.status_code, status.HTTP_204_NO_CONTENT)

        response_confirm = self.client.get(url_p)
        self.assertEqual(response_confirm.status_code, status.HTTP_404_NOT_FOUND)
