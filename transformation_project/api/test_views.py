from django.test import TestCase
from rest_framework.test import APIClient


class SortNumbersTests(TestCase):
    """
    Test cases for the sort-numbers API endpoint.
    """
    def setUp(self):
        """
        Set up the test client for API requests.
        """
        self.client = APIClient()

    def test_valid_input(self):
        """
        Test that the API correctly sorts a valid list of numbers.
        
        Sends a POST request with a list of numbers and checks that the response
        status code is 200 and the sorted list is returned in the response data.
        """
        response = self.client.post('/api/sort-numbers/', {'numbers': [3, 1, 4]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'sorted_numbers': [1, 3, 4]})

    def test_invalid_input(self):
        """
        Test that the API returns a 400 status code for invalid input.
        
        Sends a POST request with an invalid input (non-list) and checks that the 
        response status code is 400 and the response data contains an error message 
        related to the 'numbers' field.
        """
        response = self.client.post('/api/sort-numbers/', {'numbers': "not_a_list"})
        self.assertEqual(response.status_code, 400)
        self.assertIn('numbers', response.data)
