try:
    set1 = set(map(int, input("Введите числа для 1 набора: ").split()))
    set2 = set(map(int, input("Введите числа для 2 набора: ").split()))
    common = set1.intersection(set2)
    print("Общие числа: ", *common)
except ValueError:
    print("Неправильный ввод. Пожплуйста вводите только целые числа.")
