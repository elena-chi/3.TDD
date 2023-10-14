import unittest

def solve(a, b, c):
    discriminant = b**2 - 4*a*c
    if abs(discriminant) < 1e-9:
        return [-b / (2*a)]
    elif discriminant > 0:
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
        return [x1, x2]
    else:
        return []

class TestQuadraticEquation(unittest.TestCase):
    def test_double_root(self):
        # Уравнение x^2 - 2x + 0.00000001 = 0
        a = 1
        b = -2
        c = 0.00000001
        epsilon = 1e-9  # Задаем эпсилон для сравнения

        # Проверка, что уравнение имеет один корень кратности 2 (x1 = x2 = -1)
        result = solve(a, b, c)
        self.assertEqual(len(result), 1, "Ожидается один корень")
        self.assertAlmostEqual(result[0], -1, delta=epsilon, "Ожидается один корень кратности 2: x1 = x2 = -1")

if __name__ == '__main__':
    unittest.main()
