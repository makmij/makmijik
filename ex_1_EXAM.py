import random

# Запрос размеров матрицы
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

# Создание матрицы с случайными значениями
matrix = [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]

# Вывод матрицы
for row in matrix:
    print(row)

# Поиск строки с минимальной суммой элементов, содержащей и положительные, и отрицательные элементы
min_sum = float("inf")  # Сумма элементов строки, инициализируем максимально возможным значением
min_row = None  # Номер строки с минимальной суммой элементов. Делаем это чтобы после поиска мин суммы ни одна строка не соответствовала этим условиям

for i, row in enumerate(matrix): # возвращает индекс строки i и строку row
    positive_present = False
    negative_present = False
    row_sum = sum(row)

    # Проверка наличия положительных и отрицательных значений в строке
    for element in row:
        if element > 0:
            positive_present = True
        elif element < 0:
            negative_present = True

    # Проверка суммы элементов и условия наличия положительных и отрицательных значениях
    if positive_present and negative_present and row_sum < min_sum:
        min_sum = row_sum
        min_row = i

# Вывод строки с минимальной суммой элементов, содержащей и положительные, и отрицательные элементы
if min_row is not None:
    print("Строка с минимальной суммой элементов, содержащая и положительные, и отрицательные элементы:")
    print(matrix[min_row])
else:
    print("Нет строк, содержащих и положительные, и отрицательные элементы")