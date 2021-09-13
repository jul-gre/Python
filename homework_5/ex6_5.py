'''никак не получается просуммировать часы'''

d = {}
with open("text_ex_6_5.txt",encoding='utf-8' ) as file:
    for line in file:
        key, *value = line.split()
        d[key] = value
    print(d)
