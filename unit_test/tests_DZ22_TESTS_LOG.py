import unittest
from unit_test.DZ22_TESTS_LOG import Calculator
import logging
logging.basicConfig(level=logging.WARNING, filename="logs.log", filemode='w',
format="We have some error: %(asctime)s : %(levelname)s : %(message)s")
class TestDZ22(unittest.TestCase):
    def setUp(self):
        self.c1 = Calculator()
    def test_add(self):
        self.assertEqual(self.c1.add(5,5),10)
    def test_substract(self):
        self.assertEqual(self.c1.subtract(10, 5), 5)
    def test_multiply(self):
        self.assertEqual(self.c1.multiply(10,10), 100)
    def test_divide(self):
        self.assertEqual(self.c1.divide(10,0), 1)
    def test_maximum(self):
        self.assertEqual(self.c1.maximum(10,20), 20)
    def test_minimum(self):
        self.assertEqual(self.c1.minimum(10,20), 10)
    def test_percentage(self):
        self.assertEqual(self.c1.percentage(10,20), 2)
    def test_power(self):
        self.assertEqual(self.c1.power(10,2), 100)


if __name__ == '__main__':
    unittest.main()

