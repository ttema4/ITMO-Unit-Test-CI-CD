import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(4, 5), 20)
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(0, 0), 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-4, 5)

    def test_perimeter(self):
        self.assertEqual(perimeter(4, 5), 18)
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(0, 0), 0)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-4, 5)

if __name__ == '__main__':
    unittest.main()
