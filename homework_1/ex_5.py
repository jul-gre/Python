proceeds = int(input('Выручка: '))
costs = int(input('Издержки: '))
c = int(input('Численность сотрудников: '))
if proceeds > costs:
    print('Финансовый результат - прибыль')
    profit = proceeds - costs
    rent = profit / proceeds
    print('Рентабельность: ', rent)
    c_1 = profit/c
    print('Прибыль фирмы в расчете на одного сотрудника: ', c_1)
else:
    print('Финансовый результат - убыток')


