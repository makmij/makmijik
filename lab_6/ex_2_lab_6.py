def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"Введите {cols} элементов {i + 1}-й строки через пробел: ").split()))
                if len(row) != cols:
                    raise ValueError("Количество элементов в строке не соответствует заданному")
                matrix.append(row)
                break
            except ValueError as e:
                print(f"Ошибка: {e}")
    return matrix


def multiply_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            val = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))
            row.append(val)
        result.append(row)
    return result


def main():
    try:
        m = int(input("Введите количество строк для первой матрицы (M): "))
        k = int(input("Введите количество столбцов для первой матрицы и количество строк для второй матрицы (K): "))
        n = int(input("Введите количество столбцов для второй матрицы (N): "))
        if m <= 0 or k <= 0 or n <= 0:
            raise ValueError("Введены нулевые матрицы")
    except ValueError as e:
        print(e)

    print("Введите элементы первой матрицы:")
    matrix1 = input_matrix(m, k)
    print("Введите элементы второй матрицы:")
    matrix2 = input_matrix(k, n)
    result = multiply_matrices(matrix1, matrix2)
    print("Результат умножения матриц:")
    for row in result:
        print(' '.join(map(str, row)))


main()