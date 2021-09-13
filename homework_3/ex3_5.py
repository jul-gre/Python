def my_string ():
    my_sum = 0
    stop = False
    while stop == False:
        number = input('Введите G для завершения работы или вводите числа - ').split()
        res = 0
        for i in range(len(number)):
            if number[i] == 'G':
                stop = True
                break
            else:
                res = res + int(number[i])
        my_sum = my_sum + res
        print(f'Сумма на данный момент {my_sum}')
    print(f'Окончательная сумма {my_sum}')
my_string()