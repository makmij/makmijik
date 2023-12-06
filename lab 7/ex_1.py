text = input("Введите строку текста: ")
count = set(text)
if count == 0 or count == 1:
    print("Введена пустая строка или 1 символ")
else:
    print("Количество уникальных символов:", *count)