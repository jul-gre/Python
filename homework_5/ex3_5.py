with open('text_ex_3_5.txt', 'r',encoding='utf-8') as file:
    surname = []
    salary = []
    content = file.read().split('\n')

    for i in content:
        i = i.split()
        if int(i[1]) < 20000:
            salary.append(i[0])
            surname.append(i[1])
    print(f'ЗП меньше 20.000 - {salary}')

    average = sum(map(int, surname)) / len(salary)
    print(average)