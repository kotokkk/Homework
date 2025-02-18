"""
Написать генератор последовательности Фибоначчи, 
который принимает максимальное количество чисел в последовательности 
из чисел Фибоначчи и генерирует последовательность. 
Затем  вывести на экран элементы данного генератора. 
Фибоначчи последовательность - первые два числа которой являются 0 и 1, 
а каждое последующее за ними число является суммой двух предыдущих. 
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 и так далее.  
"""


def fib(n):
    """
    Генератор чисел Фибоначчи.

    Генерирует последовательность чисел Фибоначчи до n-го числа включительно.

    Аргументы:
        n (int): Количество чисел Фибоначчи, которые необходимо сгенерировать (включая 0).

    Возвращает:
        generator: Генератор, выдающий числа Фибоначчи.
    """

    a, b = 0, 1
    for _ in range(n+1):
        yield a
        a, b = b, a + b
    
num = 10
fib_g = fib(num)

print(list(fib_g))





import itertools

def fib():
    """
    Генератор чисел Фибоначчи.

    Бесконечно генерирует последовательность чисел Фибоначчи, начиная с 0.

    Возвращает:
        generator: Генератор, выдающий числа Фибоначчи.
    """

    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

num = 10

print(list(itertools.islice(fib(), num + 1)))
