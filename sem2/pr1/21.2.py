def mat_gipoteza(n):
    posled = [n]
    while n != 1:
        print(n, end='->')
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        posled.append(n)

    max_v_posled = max(posled)

    return len(posled), posled, max_v_posled




while True:
    try:
        number = int(input("Введите натуральное число N: "))
        if number > 0:
            break
        else:
            print("Пожалуйста, введите натуральное число (больше нуля).")
    except ValueError:
        print("Ошибка. Пожалуйста, введите целое натуральное число.")

res = mat_gipoteza(number)
print(f"Последовательность: {res[1]}")
print(f"Количество элементов в последовательности: {res[0]}")
print(f"Пик последовательности: {res[2]}")
