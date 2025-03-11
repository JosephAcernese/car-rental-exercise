from django.test import TestCase
import json

# Create your tests here.
class TestReservation(TestCase):

    def test_reservations_get(self):
        '''
        Test get request for reservations, expect OK response
        '''

        response = self.client.get('/reservations/')
        self.assertEqual(response.status_code, 200)


    def test_reservations_post(self):
        '''
        Test post request for reservations, expect created response
        '''

        vehicle_json = json.dumps({ "v_type" : "suv", "plate_number" : "testplate"})
        reservation_json = json.dumps({ "v_type" : "suv", "start_time" : "20250401T12:00", "end_time" : "20250404T12:00"})

        response = self.client.post('/vehicles/', data = vehicle_json, content_type="application/json")
        self.assertEqual(response.status_code, 201)

        response = self.client.post('/reservations/', data = reservation_json, content_type="application/json")
        self.assertEqual(response.status_code, 201)

        
    def test_unavailable_reservations_post(self):
        '''
        Test post request for a reservation with a v_type not available at given time
        '''
        
        vehicle_json = json.dumps({ "v_type" : "suv", "plate_number" : "testplate"})

        #Reservation JSON objects have overlapping time
        first_reservation_json = json.dumps({ "v_type" : "suv", "start_time" : "20250401T12:00", "end_time" : "20250404T12:00"})
        second_reservation_json = json.dumps({ "v_type" : "suv", "start_time" : "20250402T12:00", "end_time" : "20250406T12:00"})

        response = self.client.post('/vehicles/', data = vehicle_json, content_type="application/json")
        self.assertEqual(response.status_code, 201)


        response = self.client.post('/reservations/', data = first_reservation_json, content_type="application/json")
        self.assertEqual(response.status_code, 201)


        response = self.client.post('/reservations/', data = second_reservation_json, content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_reservation_delete(self):
        '''
        Test delete request, expect no content response
        '''

        vehicle_json = json.dumps({ "v_type" : "suv", "plate_number" : "testplate"})
        reservation_json = json.dumps({ "v_type" : "suv", "start_time" : "20250401T12:00", "end_time" : "20250404T12:00"})


        response = self.client.post('/vehicles/', data = vehicle_json, content_type="application/json")
        self.assertEqual(response.status_code, 201)

        response = self.client.post('/reservations/', data = reservation_json, content_type="application/json")
        self.assertEqual(response.status_code, 201)

        response_data = response.json()
        self.assertIn("id", response_data)
        res_id = response_data["id"]

        response = self.client.delete(f'/reservations/{res_id}/', data = vehicle_json, content_type="application/json")
        self.assertEqual(response.status_code, 204)

