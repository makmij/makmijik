def find_mode(arr):
    if not arr:
        raise ValueError("Массив пуст")

    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    max_count = max(counts.values())
    mode = []
    for num, count in counts.items():
        if count == max_count:
            mode.append(num)

    if len(mode) != 1:
        raise ValueError("Массив не уникален")

    return max_count, mode[0] # return количество и число


try:
    arr = list(map(int, input("Введите массив: ").split()))
    mode = find_mode(arr)
    print(mode[0], "раз(а) встречается число", mode[1])
except ValueError as e:
    print("Ошибка: ", e)