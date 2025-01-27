'''
Дан список:
[1, 1, 2, 3, 21, 8, 13, 21, 34, 55, 89]
вывести на экран:
    - минимальное значение
    - максимальное значение
    - сумму всех элементов
    - список только элементов с нечетным индексом
'''

numbers = [1, 1, 2, 3, 21, 8, 13, 21, 34, 55, 89]

print("Максимальное значение:", max(numbers))
print("Минимальное значение:", min(numbers))
print("Сумма всех элементов:", sum(numbers))
print("Элементы с нечетным индексом:", numbers[1::2])