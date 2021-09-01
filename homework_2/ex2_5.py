my_list = [7, 5, 3, 3, 2]
print('Рейтинг: ', my_list)
n = int(input('Введите новый элемент рейтинга: '))
for i in range(len(my_list)):
    if my_list[i] > n > my_list[i + 1]:
        my_list.insert(i + 1, n)
    elif my_list[0] < n:
        my_list.insert(0, n)
    elif my_list[-1] > n:
        my_list.append(n)
    elif my_list[i] == n:
        my_list.insert(i + 1, n)
        break
print('Новый рейтинг: ', my_list)
