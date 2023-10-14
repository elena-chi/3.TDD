import unittest

class TestQuadraticEquation(unittest.TestCase):
    def test_double_root(self):
        # Уравнение x^2 + 2x + 1 = 0
        a = 1
        b = 2
        c = 1

        discriminant = b**2 - 4*a*c

        # Вычисление корней
        if discriminant < 0:
            roots = []  # Нет корней
        elif discriminant == 0:
            x1 = -b / (2*a)
            roots = [x1, x1]
        else:
            x1 = (-b + discriminant**0.5) / (2*a)
            x2 = (-b - discriminant**0.5) / (2*a)
            roots = [x1, x2]

        # Проверка, что корни равны ожидаемому значению -1
        self.assertEqual(roots, [-1, -1], "Ожидается один корень кратности 2: x1 = x2 = -1")

if __name__ == '__main__':
    unittest.main()
