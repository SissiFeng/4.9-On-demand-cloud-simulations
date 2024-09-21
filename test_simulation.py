import unittest
from simulator import simulate_material_property

class TestSimulator(unittest.TestCase):
    
    def test_simulate_material_property(self):
        composition = {"Fe": 0.7, "C": 0.3}
        temperature = 1000
        
        result = simulate_material_property(composition, temperature)
        
        self.assertIsInstance(result, float)
        self.assertGreater(result, 0)
    
    # TODO: Add more test cases to cover different scenarios
    
if __name__ == '__main__':
    unittest.main()
