from math import *


def get_angle():
    while True:
        try:
            angle = float(input("Введите угол в градусах: "))
            return angle
        except ValueError:
            print("Ошибка! Введите число.")


angle = get_angle()
print('Синус угла:', sin(angle))
print('Косинус угла:', cos(angle))
print('Тангенс угла:', tan(angle))
