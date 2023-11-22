import math


def gcd(a, b):
    if a < 0 or b < 0:
        raise ValueError("Числа должны быть натуральными")
    while b != 0:
        a, b = b, a % b
    return a

def own_imput():
    while True:
        try:
            a = int(input("Введите первое число: "))
            b = int(input("Введите второе число: "))
            return a, b
        except ValueError:
            print("Введено не число")

try:
    a, b = own_imput()
    result = gcd(a, b)
    print("НОД чисел", a, "и", b, ":", result)
    math_result = math.gcd(a, b)
    if result == math_result:
        print("Результат совпадает с результатом из библиотеки math")
    else:
        print("Результат не совпадает с результатом из библиотеки math")
except ValueError as e:
    print("Ошибка:", e)