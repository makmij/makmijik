words = input("Введите 10 слов, разделённых точкой с запятой: ").split(';')

if len(words) != 10:
    print("Ошибка: нужно ввести 10 слов.")
else:
    control_str = input("Введите контрольную строку: ")
    found_words = [word.strip() for word in words if word.strip().startswith(control_str)]

    for found_word in found_words:
        print("Совпадение:", found_word)