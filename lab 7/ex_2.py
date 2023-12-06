first_string = input("Введите первую строку: ")
second_string = input("Введите вторую строку: ")
first_set = set(first_string)
second_set = set(second_string)
if len(first_set) == 0 or len(second_set) == 0:
    print("Введена пустая строка")
else:
    unique_chars = first_set - second_set
    print(*unique_chars)