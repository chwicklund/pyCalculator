import unittest
from helpers.RandomGenerator import RandomGenerator
from src.calculator.calculator import Calculator


class RandomGeneratorTestCase(unittest.TestCase):
    def test_random_generator(self):
        random_number = RandomGenerator.get_random_number(4)
        self.assertEqual(random_number, 4)
