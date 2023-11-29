import re


def check_filename(filename):
    if not filename.endswith(('.txt', '.doc', '.docx', '.odt', '.rtf')):
        return False
    if re.search(r'[<>/\|?*]', filename):
        return False
    return True


while True:
    filename = input("Введите имя файла (для завершения введите пустую строку): ")
    if filename == '':
        break
    if check_filename(filename):
        print("Введенное имя файла корректно.")
    else:
        print("Введенное имя файла некорректно.")