sec = int (input('Введите время в секундах: '))
hours = sec // 3600
min = sec // 60
print (hours, ':', min,' :', sec,)


sec = int (input('Введите время в секундах: '))
hours = sec // 3600
min = sec // 60
print('{}:{}:{}'.format(hours, min, sec))