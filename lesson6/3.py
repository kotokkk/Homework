'''
Запросить 3 числа. Вывести наибольшее  из них. Решить используя if.
'''

#Первое что пришло на ум
first = float(input("Введите число №1: "))
second = float(input("Введите число №2: "))
third = float(input("Введите число №3: "))


if second<first>third:
    print(first)
elif first<second>third:
    print(second)
else:
    print(third)



#Попрактиковала через список

# numb = input("Введите 3 числа через пробел: ")

# a = list(map(float,numb.split()))

# if a[1]<a[0]>a[2]:
#     print(a[0])
# elif a[0]<a[1]>a[2]:
#     print(a[1])
# else:
#     print(a[2])





#Через тернарный оператор

# first = float(input("Введите число №1: "))
# second = float(input("Введите число №2: "))
# third = float(input("Введите число №3: "))


# n = first if (third<=first>=second) else (second if (first<=second>=third ) else third)

# print(f"Наибольшее число из введенных: {n}")