import unittest

class TestQuadraticEquation(unittest.TestCase):
    def test_a_not_zero(self):
        # Проверка, что a не равно 0
        a = 2.0  # Пример ненулевого значения коэффициента a
        b = 1.0
        c = 1.0

        # Если a равно 0, вызовет исключение AssertionError
        self.assertNotEqual(a, 0, "Коэффициент a не может быть равен 0")

if __name__ == '__main__':
    unittest.main()
