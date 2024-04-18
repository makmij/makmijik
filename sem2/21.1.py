words = input("Введите слова, разделённые точкой с запятой: ").split(';')
control_str = input("Введите контрольное слово: ")
found_words = [word.strip() for word in words if word.strip().startswith(control_str)]

for found_word in found_words:
    print("Совпадение:",found_word)