import unittest
import math

def sqrt(x : int) -> int:
    return math.floor(math.sqrt(x))

class TestSqrt(unittest.TestCase):
    def test_squares(self):
        for i in range(100):
            self.assertEqual(i, sqrt(i**2))
    
    def test_negative(self):
        self.assertRaises(ValueError, sqrt, -1)
        
    def test_large_number(self):
        n = 1234567899876543210
        self.assertAlmostEqual(sqrt(n**2), n, places=-3)
    
    def test_integers(self):
        for i in range(100):
            self.assertEqual(sqrt(i), math.floor(math.sqrt(i)))

if __name__ == "__main__":
    unittest.main(verbosity=1)