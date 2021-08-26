i = 1
result_1 = int(input())
result_2 = int(input())
while result_1 <= result_2:
    result_1 = result_1 + (result_1 * 0.1)
    i += 1
print('На ', i, 'день бегун пробежал', result_1, 'км')
