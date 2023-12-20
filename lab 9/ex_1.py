def remove_from_end(numbers, num_to_remove):
    if len(numbers) >= num_to_remove:
        numbers = numbers[:-num_to_remove]
    return numbers

# Чтение вектора из файла

with open("input.txt", "r") as file:
    vector = list(map(float, file.readline().split()))

# Заданное количество чисел для удаления
while True:
    try:
        num_to_remove = int(input())
        break
    except ValueError:
        print("Введено не число")

# Удаление чисел из конца вектора
new_vector = remove_from_end(vector, num_to_remove)

# Проверка на корректность данных
if len(vector) < num_to_remove:
    print("Количество чисел для удаления больше размера вектора.")
else:
    # Запись нового вектора в отдельный файл
    with open("output.txt", "w") as file:
        file.write(" ".join(map(str, new_vector)))
        print("Новый вектор записан в файл 'output.txt'.")