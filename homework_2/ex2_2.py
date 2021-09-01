my_list = []
n = int(input('Количество элементов в списке: '))
for i in range(n):
    x = int(input('Добавьте элементы в список: '))
    my_list.append(x)
print(my_list)
if len(my_list)%2!=0:
    print('Список не изменен', my_list)
elif len(my_list)%2==0:
    for i in range(len(my_list)):
        my_list[i], my_list[i-1]=my_list[i-1], my_list[i]
    print('Новый список: ', my_list)