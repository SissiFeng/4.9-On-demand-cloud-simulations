import unittest
import json
from lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):
    
    def test_lambda_handler(self):
        # Simulate a Lambda event
        test_event = {
            'composition': {'Fe': 0.7, 'C': 0.3},
            'temperature': 1000
        }
        
        # Call the lambda_handler
        response = lambda_handler(test_event, None)
        
        # Check the response format
        self.assertEqual(response['statusCode'], 200)
        
        # Parse the response body
        body = json.loads(response['body'])
        
        # Check if the response body contains 'simulated_property'
        self.assertIn('simulated_property', body)
        
        # Check if 'simulated_property' is a float
        self.assertIsInstance(body['simulated_property'], float)
        
        # Additional assertions can be added here to check specific simulation result values

if __name__ == '__main__':
    unittest.main()
