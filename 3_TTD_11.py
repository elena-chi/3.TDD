import unittest

class TestQuadraticEquation(unittest.TestCase):
    def test_double_root(self):
        # Уравнение x^2 - 2x + 0.01 = 0
        a = 1
        b = -2
        c = 0.01
        discriminant = b**2 - 4*a*c
        epsilon = 1e-9  # Задаем эпсилон

        # Проверка, что дискриминант близок к нулю, но не равен ему
        self.assertLess(discriminant, epsilon, "Дискриминант близок к нулю, но не равен ему")

        # Проверка, что уравнение имеет один корень кратности 2 (x1 = x2 = -1)
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
        self.assertAlmostEqual(x1, -1, delta=epsilon, "Ожидается один корень кратности 2: x1 = -1")
        self.assertAlmostEqual(x2, -1, delta=epsilon, "Ожидается один корень кратности 2: x2 = -1")

if __name__ == '__main__':
    unittest.main()