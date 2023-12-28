first_string = input("Введите первую строку: ")
second_string = input("Введите вторую строку: ")
if second_string in first_string:
    a=first_string.replace(second_string, '', first_string.count(second_string)-1)
    print(a)
else:
    print(first_string)