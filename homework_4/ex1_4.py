from sys import argv
vyr_v_chasah, stavka_1, premia = argv
vyr_v_chasah = int(input())
stavka_1 = int(input())
premia = int(input())
res = (vyr_v_chasah * stavka_1) + premia
print(f'з/п - {res}')