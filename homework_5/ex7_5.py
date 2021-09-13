import json
profit = {}
prof = 0
average = 0
i = 0
with open('text_ex_7_5.txt', 'r', encoding='utf-8') as file:
    for line in file:
        name, firm, money, ubytok = line.split()
        profit[name] = int(money) - int(ubytok)
        if profit.get(name) >= 0:
            prof = prof + profit.get(name)
            i += 1
        average = prof / i
    print(f'Средняя прибыль каждой компании - {profit}')

with open('text_ex_7_5_jsoon).json', 'w') as js:
    json.dump(profit, js)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js}')