import unittest
from main import find_number_index

class TestFindNumberIndex(unittest.TestCase):
    
    def test_number_found(self):
        numbers = [10, 20, 30, 40, 50]
        X = 30
        result = find_number_index(numbers, X)
        self.assertEqual(result, 3)

    def test_number_not_found(self):
        numbers = [10, 20, 30, 40, 50]
        X = 60
        result = find_number_index(numbers, X)
        self.assertEqual(result, -1)

    def test_first_position(self):
        numbers = [10, 20, 30, 40, 50]
        X = 10
        result = find_number_index(numbers, X)
        self.assertEqual(result, 1)

    def test_last_position(self):
        numbers = [10, 20, 30, 40, 50]
        X = 50
        result = find_number_index(numbers, X)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()