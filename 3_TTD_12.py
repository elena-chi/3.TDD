import unittest

class TestQuadraticEquation(unittest.TestCase):
    def test_double_root(self):
        # Уравнение x^2 - 4x + 4.01 = 0
        a = 1
        b = -4
        c = 4.01
        epsilon = 1e-9  # Задаем эпсилон для сравнения

        # Проверка, что уравнение имеет один корень кратности 2 (x1 = x2 = -2)
        x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
        x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
        self.assertAlmostEqual(x1, -2, delta=epsilon, "Ожидается один корень кратности 2: x1 = -2")
        self.assertAlmostEqual(x2, -2, delta=epsilon, "Ожидается один корень кратности 2: x2 = -2")

if __name__ == '__main__':
    unittest.main()
