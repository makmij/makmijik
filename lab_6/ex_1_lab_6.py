def scalar_product(vector1, vector2):

    result = 0
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]
    return result


def input_vector():
    vector = []
    while True:
        try:
            n = int(input("Введите размер вектора: "))
            break
        except ValueError:
            print("Введено не число")
    for i in range(n):
        while True:
            try:
                value = int(input(f"Введите {i + 1}й элемент вектора: "))
                vector.append(value)
                break
            except ValueError:
                print("Введено не число")
    return vector


print("Первый вектор")
vector1 = input_vector()
print("Второй вектор")
vector2 = input_vector()
if len(vector1) != len(vector2):
    print("Размеры вектора не равны")
else:
    product = scalar_product(vector1, vector2)
    print("Скалярное произведение двух векторов равно:", product)