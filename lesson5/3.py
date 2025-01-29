"""
дан словарь
d = {'one':11, 'two':22, 'hello':'python', True:False}
запросить номер элемента и удалить его из словаря с помощью del.

"""

d = {'one':11, 'two':22, 'hello':'python', True:False}

num = int(input("Введите номер элемента для удаления (начиная с 0): "))

keys = list(d.keys())
del d[keys[num]]

print(d)
