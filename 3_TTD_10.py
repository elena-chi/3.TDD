import unittest

def solve(a, b, c):
    if a == 0:
        raise ValueError("Коэффициент a не может быть равен 0")
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []  # Нет корней
    x1 = (-b + (discriminant)**0.5) / (2*a)
    x2 = (-b - (discriminant)**0.5) / (2*a)
    return [x1, x2]

class TestQuadraticEquation(unittest.TestCase):
    def test_a_not_zero(self):
        # Проверка, что solve выбрасывает исключение, если a равно 0
        a = 0
        b = 2
        c = 1
        with self.assertRaises(ValueError):
            solve(a, b, c)

if __name__ == '__main__':
    unittest.main()