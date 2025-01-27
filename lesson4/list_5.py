'''
Дан список
['samsung', 'lg', 'xerox', 'bosch']
Удалить элемент с именем 'xerox'
Добавить элемент на 2 место 'indesit'

'''
brands = ['samsung', 'lg', 'xerox', 'bosch']

brands.remove('xerox')
brands.insert(1, 'indesit')

print("Отредактированный список: ", brands)