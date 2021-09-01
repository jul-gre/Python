goods = []
des = {}
des_title = input('Ввведите название товара: ')
des_price = input('Введите цену товара: ')
des_amount = input('Введите количество: ')
des_value = input('Введите единицу измерения: ')
goods.append({'title': des_title, 'price': des_price, 'amount': des_amount, 'value': des_value})
analys = {'title': [], 'price': [], 'amount': [], 'value': set()}
for item in goods:
    analys['title'].append(item['title'])
    analys['price'].append(item['price'])
    analys['amount'].append(item['amount'])
    analys['value'].add(item['value'])
print('Аналитика о товаре: ', analys)
