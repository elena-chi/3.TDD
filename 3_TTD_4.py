import math
def solve(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []  # Нет корней
    elif discriminant == 0:
        x = -b / (2*a)
        return [x]
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return [x1, x2]
# Тест для уравнения x^2 + 1 = 0 
a = 1
b = 0
c = 1
result = solve(a, b, c)
expected_result = []
if result == expected_result:
    print("Тест пройден: Решение уравнения x^2 + 1 = 0 верное")
else:
    print("Тест не пройден: Решение уравнения x^2 + 1 = 0 неверное")
# Тест завершен
