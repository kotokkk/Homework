'''
Программа должна запросить несколько цифр через пробел 
    - выдать их общую сумму
    - выдать максимальную цифру
    - выдать среднее арифметическое

'''

nums = input("Введите цифры через пробел: ")

new_list = nums.split()
numbers = list(map(int,new_list))
s = sum(numbers)
m_num = max(numbers)
lenth_1 = len(numbers)
average = s / lenth_1
print(f"Общая сумма цифр: {s} \nМаксимальная цифра из списка: {m_num} \nСреднее арифметическое: {average}")

