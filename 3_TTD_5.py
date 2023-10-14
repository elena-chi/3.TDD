import unittest

class TestQuadraticEquation(unittest.TestCase):
    def test_two_roots(self):
        # Уравнение x^2 - 1 = 0
        a = 1
        b = 0
        c = -1

        discriminant = b**2 - 4*a*c

        # Вычисление корней
        if discriminant < 0:
            roots = []  # Нет корней
        else:
            x1 = (-b + discriminant**0.5) / (2*a)
            x2 = (-b - discriminant**0.5) / (2*a)
            roots = [x1, x2]

        # Проверка, что корни равны ожидаемым значениям
        self.assertEqual(roots, [1, -1], "Ожидается два корня кратности 1: x1=1, x2=-1")

if __name__ == '__main__':
    unittest.main()
