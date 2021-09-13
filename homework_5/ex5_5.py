with open('text_ex_5_5.txt', 'w') as f:
    string = input('Введите цифры: ')
    f.writelines(string)
    number = string.split()
    print(f)
    print(sum(map(int, number)))