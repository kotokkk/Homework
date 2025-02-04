"""
Даны 4 переменные - a1, a2, a3, a4.
1 - вывести True если все они дробные числа
2 - вывести True если одна из них строка
3 - вывести True если  одна пара переменных является целочисленным типом. 
    Пары могут образовать только следующие переменные - a1-a3, a2-a4, a3-a4"
"""



a1 = 1.5
a2 = "Hello"
a3 = 2.3
a4 = 4

if isinstance(a1, float) and isinstance(a2, float) and isinstance(a3, float) and isinstance(a4, float):
    print("Все переменные дробные числа: True")
else:
    print("Все переменные дробные числа: False")

if isinstance(a1, str) or isinstance(a2, str) or isinstance(a3, str) or isinstance(a4, str):
    print("Одна из переменных строка: True")
else:
    print("Одна из переменных строка: False")

if (isinstance(a1, int) and isinstance(a3, int)) or \
   (isinstance(a2, int) and isinstance(a4, int)) or \
   (isinstance(a3, int) and isinstance(a4, int)):
    print("Есть пара целочисленных типов: True")
else:
    print("Есть пара целочисленных типов: False")
