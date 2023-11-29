import re


def is_valid_car_number(input_str):
    if len(input_str) != 6:
        print("Неверная длина строки. Должно быть 6 символов")
        return False
    pattern = re.compile(r'^[A-Za-z]{2}\d{3}[A-Za-z]$') # ^ - начало строки, [A-Za-z] - любая буква от A до Z, {2} - повторение пред символа 2 раза, \d означает любую цифру, {3} - повторение пред символа 3 раза, $ - конец строки
    if not pattern.match(input_str):
        print("Неверный формат строки. Должны быть 2 буквы, 3 цифры и 1 буква")
        return False
    if not input_str[:2].isalpha() or not input_str[-1].isalpha():
        print("Неверные буквы. Должны быть только латинские буквы")
        return False
    return True


input_str = input("Введите номер автомобиля (две буквы, три цифры, одна буква): ")

if is_valid_car_number(input_str):
    print("Введенная строка является номером автомобиля.")
else:
    print("Введенная строка не является номером автомобиля.")