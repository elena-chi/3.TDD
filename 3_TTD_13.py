import unittest
import math

class TestQuadraticEquation(unittest.TestCase):
    def test_a_nan(self):
        # Проверка, что solve выбрасывает исключение, если a = NaN
        a = math.nan
        b = 2.0
        c = 1.0
        with self.assertRaises(ValueError):
            solve(a, b, c)

    def test_b_nan(self):
        # Проверка, что solve выбрасывает исключение, если b = NaN
        a = 1.0
        b = math.nan
        c = 1.0
        with self.assertRaises(ValueError):
            solve(a, b, c)

    def test_c_nan(self):
        # Проверка, что solve выбрасывает исключение, если c = NaN
        a = 1.0
        b = 2.0
        c = math.nan
        with self.assertRaises(ValueError):
            solve(a, b, c)

    def test_a_infinity(self):
        # Проверка, что solve выбрасывает исключение, если a = Infinity
        a = math.inf
        b = 2.0
        c = 1.0
        with self.assertRaises(ValueError):
            solve(a, b, c)

    def test_b_infinity(self):
        # Проверка, что solve выбрасывает исключение, если b = Infinity
        a = 1.0
        b = math.inf
        c = 1.0
        with self.assertRaises(ValueError):
            solve(a, b, c)

    def test_c_infinity(self):
        # Проверка, что solve выбрасывает исключение, если c = Infinity
        a = 1.0
        b = 2.0
        c = math.inf
        with self.assertRaises(ValueError):
            solve(a, b, c)