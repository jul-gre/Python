from math import *
from itertools import cycle, count
def fact(n):
    for i in range(1, n+1):
        yield factorial(i)
count = int(input('Введите количество необходимых факториалов '))
for el in fact(count):
    print(el)
