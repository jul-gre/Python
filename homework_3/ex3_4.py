def my_func(x,y):
    return x**y
x = int(input('Enter "+" number: '))
y = int(input('Enter "-" number '))
print(f'Result - {my_func(x,y)}')

def my_func(x,y): #without standart operation
    return pow(x,y)
x = int(input('Enter "+" number: '))
y = int(input('Enter "-" number '))
print(f'Result - {my_func(x,y)}')