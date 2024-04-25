import re
from collections import Counter

def count_char_frequency(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read().lower()
            data = re.sub(r'[^a-zA-Zа-яА-Я]', '', data)  # оставляем только буквы, убирая остальные символы

            char_freq = Counter(data)

            with open('res1.txt', 'w', encoding='utf-8') as res_file:
                for char, freq in char_freq.items():
                    res_file.write(f"{char}: {freq}\n")

            print("Результат успешно записан в файл res1.txt")

    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


file_path = 'res1.txt'
count_char_frequency(file_path)