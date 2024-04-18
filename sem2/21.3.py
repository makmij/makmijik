import re


# Функция для чтения данных из файла и парсинга информации
def read_file(path):
    data = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            match = re.findall(r'\S+', line)
            if len(match) >= 2:
                name = match[0]
                score = int(match[1])
                data.append((name, score))
    return data


# Функции для сортировки участников по имени и по баллам
def sort_by_name(data):
    return sorted(data, key=lambda x: x[0])


def sort_by_score(data):
    return sorted(data, key=lambda x: x[1])


# вывод на консоль и сохранение в файл
def output_participants(data, path, porog):
    filtered_data = filter(lambda x: x[1] > porog, data)

    with open(path, 'w', encoding='utf-8') as file:
        for item in filtered_data:
            file.write(item[0] + "\n")


path = "res.txt"
porog = int(input("Введите порог фильтр по участникам: "))

try:
    participants = read_file(path)

    # Сортировка участников по имени
    sorted_by_name = sort_by_name(participants)
    print("Участники конкурса отсортированные по имени:")
    for item in sorted_by_name:
        print(item)

    # Сортировка участников по баллам
    sorted_by_score = sort_by_score(participants)
    print("\nУчастники конкурса отсортированные по баллам:")
    for item in sorted_by_score:
        print(item)

    # Вывод участников с результатом выше порога в файл
    output_participants(participants, "res.txt", porog)
    print(f"\nИмена участников с результатом выше {porog} сохранены в файл res.txt.")

except Exception as e:
    print(f"Произошла ошибка: {str(e)}")