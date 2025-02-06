"""
Запросить любое число не менее 10. 
Вывести на экран сумму квадратов каждой цифры составляющей это число. 
Например: дано 236 => 2*2 + 3*3 + 6*6 = 49 

"""


num = input("Введите число, не меньше 10: ")

if num.isdigit() and int(num) >= 10:
    l = [int(d)**2 for d in num]  # Создаем список квадратов цифр
    print(f'Сумма квадратов цифр: {sum(l)}')
else:
    print("err")





# l = []

# num = input("Введите число, не меньше 10: ")

# if num.isdigit():
#     b = int(num)
#     if b>=10:
#         c = list(map(int,str(b)))
#         for i in c:
#            n = i**2
#            l.append(n)
#         print(f'djjddj {sum(l)}') 
#     else:
#         print("err")
# else:
#     print("err2")
