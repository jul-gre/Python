with open('text_ex_4_5.txt', 'r',encoding='utf-8') as file:
    #content = file.readlines()
    #print(content)

    trans = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    new_file = []

    for i in file:
        i = i.split(' ', 1)
        new_file.append(trans[i[0]] + '  ' + i[1])
    print(new_file)

with open('text_ex_4_5_new.txt', 'w') as file2:
    file2.writelines(new_file)
