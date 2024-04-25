import re


def read_file(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            match = re.findall(r'\S+', line)
            if len(match) >= 2:
                name = match[0]
                score = int(match[1])
                data.append((name, score))
    return data


def output_participants(data, file_path, threshold):
    filtered_data = filter(lambda x: x[1] > threshold, data)
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in filtered_data:
            file.write(item[0] + "\n")


file_path = "res.txt"
peak = int(input("Введите пороговое значение для фильтрации участников: "))

try:
    participants = read_file(file_path)

    sorted_by_name = sorted(participants, key=lambda x: x[0])
    print("Участники конкурса отсортированные по имени:")
    for item in sorted_by_name:
        print(item)

    sorted_by_score = sorted(participants, key=lambda x: x[1])
    print("\nУчастники конкурса отсортированные по баллам:")
    for item in sorted_by_score:
        print(item)

    output_participants(participants, "res.txt", peak)
    print(f"\nИмена участников с результатом выше {peak} сохранены в файл res.txt.")

except Exception as e:
    print(f"Произошла ошибка: {str(e)}")