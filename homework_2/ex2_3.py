seasons = ['summer', 'autumn', 'winter', 'spring'] #через список
n = int(input('Enter the number of month: '))
if n == 1 or n == 2 or n == 12:
    print(seasons[2])
elif n == 3 or n == 4 or n == 5:
    print(seasons[3])
elif n == 6 or n == 7 or n == 8:
    print(seasons[0])
elif n == 9 or n == 10 or n == 11:
    print(seasons[1])
else:
    print('The number of month is not correct')

seasons_dict = {1: 'summer',2: 'autumn',3: 'winter',4: 'spring'} #через словарь
n_dict = int(input('Enter the number of month: '))
if n == 1 or n == 2 or n == 12:
    print(seasons_dict.get(3))
elif n == 3 or n == 4 or n == 5:
    print(seasons_dict.get(4))
elif n == 6 or n == 7 or n == 8:
    print(seasons_dict.get(1))
elif n == 9 or n == 10 or n == 11:
    print(seasons_dict.get(2))
else:
    print('The number of month is not correct')