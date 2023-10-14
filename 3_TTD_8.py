import math

def solve(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []  # Нет корней
    elif discriminant == 0:
        x = -b / (2*a)
        return [x, x]  # Корень кратности 2
    else:
        x = -b / (2*a)
        return [x, x]  # Корень кратности 2

# Тест для уравнения x^2 + 2x + 1 = 0
a = 1
b = 2
c = 1
result = solve(a, b, c)
expected_result = [-1, -1]  # Ожидается один корень кратности 2
if result == expected_result:
    print("Тест пройден: Решение уравнения x^2 + 2x + 1 = 0 верное")
else:
    print("Тест не пройден: Решение уравнения x^2 + 2x + 1 = 0 неверное")
