from django.test import TestCase
import json

# Create your tests here.
class TestVehicle(TestCase):
    def test_vehicles_get(self):
        '''
        Test get request for vehicles, expect OK response
        '''

        response = self.client.get('/vehicles/')
        self.assertEqual(response.status_code, 200)

    def test_vehicles_post(self):
        '''
        Test post request for vehicles, expect created response
        '''

        vehicle_json = json.dumps({ "v_type" : "suv", "plate_number" : "testpost"})

        response = self.client.post('/vehicles/', data = vehicle_json, content_type="application/json")
        self.assertEqual(response.status_code, 201)


    def test_vehicles_duplicate_post(self):
        '''
        Test two duplicate post requests, expect bad request response
        '''
        vehicle_json = json.dumps({ "v_type" : "suv", "plate_number" : "testpost"})

        response = self.client.post('/vehicles/', data = vehicle_json, content_type="application/json")
        self.assertEqual(response.status_code, 201)

        response = self.client.post('/vehicles/', data = vehicle_json, content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_vehicle_delete(self):
        '''
        Test delete request, expect no content response
        '''

        plate_number = "testpost"
        vehicle_json = json.dumps({ "v_type" : "suv", "plate_number" : plate_number})

        response = self.client.post('/vehicles/', data = vehicle_json, content_type="application/json")
        self.assertEqual(response.status_code, 201)

        vehicle_json = json.dumps({"plate_number" : plate_number})
        response = self.client.delete(f'/vehicles/{plate_number}/', data = vehicle_json, content_type="application/json")
        self.assertEqual(response.status_code, 204)
