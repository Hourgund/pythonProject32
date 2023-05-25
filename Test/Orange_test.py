import unittest
from Entity.orange import Orange


class OrangeTest(unittest.TestCase):
    def test_orange_default_constructor(self):
        orange = Orange()
        expected_diameter = 100
        expected_vitamin = 1000
        expected_price = 0

        self.assertEqual(expected_diameter, orange.diameter)
        self.assertEqual(expected_vitamin, orange.vitamin)
        self.assertEqual(expected_price, orange.price)

    def test_orange_constructor_with_args(self):
        expected_diameter = 200
        expected_vitamin = 2000
        expected_price = 15

        orange = Orange(expected_diameter, expected_vitamin, expected_price)

        self.assertEqual(expected_diameter, orange.diameter)
        self.assertEqual(expected_vitamin, orange.vitamin)
        self.assertEqual(expected_price, orange.price)

    def test_negative_diameter_orange(self):
        diameter = -200
        expected = 100
        orange = Orange(diameter=diameter)
        self.assertEqual(expected, orange.diameter)

    def test_negative_vitamin_orange(self):
        vitamin = -200
        expected = 1000
        orange = Orange(vitamin=vitamin)
        self.assertEqual(expected, orange.vitamin)

    def test_zero_diameter_orange(self):
        diameter = 0
        expected = 100

        orange = Orange(diameter=diameter)

        self.assertEqual(expected, orange.diameter)

    def test_zero_vitamin_orange(self):
        vitamin = 0
        expected = 0

        orange = Orange(vitamin=vitamin)

        self.assertEqual(expected, orange.vitamin)

    def test_zero_price_orange(self):
        price = 0
        expected = 0

        orange = Orange(price=price)

        self.assertEqual(expected, orange.price)

    def test_diameter_property_negative(self):
        orange = Orange()
        expected = orange.diameter

        orange.diameter = -200

        self.assertEqual(expected, orange.diameter)

    def test_diameter_property_positive(self):
        orange = Orange()
        expected = 200
        orange.diameter = 200
        self.assertEqual(expected, orange.diameter)

    def test_diameter_property_with_zero(self):
        orange = Orange()
        expected = orange.diameter
        orange.diameter = 0
        self.assertEqual(expected, orange.diameter)

    def test_vitamin_property_negative(self):
        orange = Orange()
        expected = orange.vitamin

        orange.vitamin = -200

        self.assertEqual(expected, orange.vitamin)

    def test_vitamin_property_positive(self):
        orange = Orange()
        expected = 200
        orange.vitamin = 200
        self.assertEqual(expected, orange.vitamin)

    def test_vitamin_property_with_zero(self):
        orange = Orange()
        expected = 0
        orange.vitamin = 0
        self.assertEqual(expected, orange.vitamin)


if __name__ == "__main__":
    unittest.main()
