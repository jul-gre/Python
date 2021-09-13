from itertools import cycle, count
def my_count_func(start, stop):
    for i in count(start):
        if i > stop:
            break
        else:
            print(i)

start = int(input('Введем первое число '))
stop = int(input('Введем последнее число'))
my_count_func(start, stop)


def my_cycle_func(my_list, it):
    i = 0
    iter = cycle(my_list)
    while i < it:
        print(next(iter))
        i+=1
my_list = [0, 1, 2, 3, 4 ,5]
it = int(input('Введем итератор '))
my_cycle_func(my_list, it)