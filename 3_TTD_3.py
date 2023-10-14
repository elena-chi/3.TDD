import unittest

class TestQuadraticEquation(unittest.TestCase):
    def test_no_roots(self):
        # Уравнение x^2 + 1 = 0
        a = 1
        b = 0
        c = 1
        discriminant = b**2 - 4*a*c
        roots = []
        if discriminant < 0:
            result = []  # Нет корней
        else:
            x1 = (-b + discriminant**0.5) / (2*a)
            x2 = (-b - discriminant**0.5) / (2*a)
            result = [x1, x2]
        self.assertEqual(result, roots, "Ожидается пустой список корней")

if __name__ == '__main__':
    unittest.main()