with open('text_ex_2_5.txt', 'r') as file:
    content = file.read()
    print(f' text of the file - {content}')
with open('text_ex_2_5.txt', 'r') as file:
    content = file.readlines()
    size = len(content)
    print(f'amount of strings - {size}')
with open('text_ex_2_5.txt', 'r') as file:
    content = file.read()
    content = content.split()
    print(f'amount of words - {len(content)}')



