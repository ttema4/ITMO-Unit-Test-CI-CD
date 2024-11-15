import unittest
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_positive(self):
        self.assertAlmostEqual(area(3), 28.274333882308138)
        self.assertAlmostEqual(area(0), 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-3)

    def test_perimeter_positive(self):
        self.assertAlmostEqual(perimeter(3), 18.84955592153876)
        self.assertAlmostEqual(perimeter(0), 0)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-3)


if __name__ == '__main__':
    unittest.main()
