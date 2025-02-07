"""
1. Запросить у пользователей имя и отзыв о магазине. 
Программа должна запрашивать данные пока не введено слово "stop". 
Все данные сложить в словарь.
    -распечатать количество отзывов
    -распечатать отдельно имена пользователей
    -распечатать отдельно отзывы

"""


import re

l_2 = []

while True:
    user_input = input("Vvedite name i user_input: ")
    if user_input == "stop".lower():
        break

    t = tuple(re.split(r'[,\s]+', user_input))
    l_2.append(t)
    reviews = {key: value for key, value in l_2}

print(f"""Количество отзывов: {len(reviews.values())}. 
Имена пользователей: {', '.join(reviews.keys())}.
Отзывы: {', '.join(reviews.values())}.
""")
    
    






#Вариант с проверкой на количество введенных слов

import re

reviews = {}

while True:
    user_input = input("Введите имя и отзыв о магазине (или 'stop' для завершения): ")
    if user_input.lower() == "stop":
        break

    parts = re.split(r'[,\s]+', user_input)
    if len(parts) == 2:
        name, review = parts
        reviews[name] = review
    else:
        print("Некорректный ввод. Введите имя и отзыв через запятую или пробел.")

print(f"""
Количество отзывов: {len(reviews)}
Имена пользователей: {', '.join(reviews.keys())}
Отзывы: {', '.join(reviews.values())}
""")



