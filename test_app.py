import unittest
from app import search_products

class TestProductSearch(unittest.TestCase):

    def test_case_insensitive_search(self):
        result = search_products("apple")
        self.assertIn("Apple Watch", result)
        self.assertIn("Pineapple Juice", result)

    def test_existing_search(self):
        self.assertIn("Banana", search_products("Ban"))

if __name__ == "__main__":
    unittest.main()
