"""
Запросить у пользователя год рождения и в соответствии с его возрастом 
охарактеризовать пользователя - 
ребенок, подросток, юноша, в расцвете сил, пожилой, старик.
"""

#сразу написала пошагово, длинная запись

# year = int(input("Введите год рождения: "))

# age = 2025 - year

# if 0<=age<=110:
#     if age<=12:
#         print("kid")
#     elif 13<=age<=17:
#         print('podrostok')
#     elif 18<=age<=24:
#         print("unosha")
#     elif 25<=age<=50:
#         print("v rasvete sil")
#     elif 51<=age<=65:
#         print("pogiloy")
#     elif 66<=age<=110:
#         print("starik")
# else:
#     print("ваш год рожденияне не подходит")




# короткий вариант
year = int(input("Введите год рождения: "))

age = 2025 - year

if 0 <= age <= 110:
    category = (
        "Вы ребенок" if age <=12 else
        "Вы подросток" if age <=17 else
        "Вы юный" if age <=24 else
        "Вы в расцвете сил" if age <=50 else
        "Вы пожилой" if age<=65 else
        "Вы старик"
    )
    print(category)
else:
    print("Ваш год рождения не подходит")




