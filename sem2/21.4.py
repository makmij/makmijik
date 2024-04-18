def char_freq(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            # Преобразование всех символов в нижний регистр
            content = content.lower()

            # Подсчет частоты встречаемости каждого символа
            char_count = {}
            for char in content:
                if char.isalpha():
                    char_count[char] = char_count.get(char, 0) + 1

            return char_count
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except PermissionError:
        print(f"Отказано в доступе к файлу {file_path}.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def save_result(file_path, char_count):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for char, count in char_count.items():
                file.write(f"{char}: {count}\n")
        print(f"Результат успешно сохранен в файле {file_path}.")
    except Exception as e:
        print(f"Произошла ошибка при сохранении результата: {e}")

file_path = input("Введите путь к файлу с текстом (с расширением .txt): ")
if not file_path.endswith('.txt'):
    print("Ошибка: Введите путь к файлу с расширением .txt.")
else:
    char_count = char_freq(file_path)
    if char_count:
        save_result('res1.txt', char_count)