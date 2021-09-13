from random import *
my_random_list = [randint (1, 10) for i in range(5) ]
i = 0
new= []
for el in my_random_list:
    if el > my_random_list[i-1]:
        new.append(el)
    i+=1
print(my_random_list)
print(new)
