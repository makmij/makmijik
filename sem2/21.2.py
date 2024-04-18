def mgip(N):
    cnt = 0
    max = N
    while N != 1:
        print(N, end='->')
        cnt += 1
        if N % 2 == 0:
            N = N // 2
        else:
            N = N * 3 + 1
        if N > max:
            max = N

    print(1)
    print("Количество элементов в последовательности:", cnt + 1)
    print("Пик последовательности:", max)


while True:
    try:
        number = int(input("Введите натуральное число N: "))
        if number > 0:
            break
        else:
            print("Пожалуйста, введите натуральное число (больше нуля).")
    except ValueError:
        print("Ошибка. Пожалуйста, введите целое натуральное число.")

mgip(number)