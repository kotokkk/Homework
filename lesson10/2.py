
"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""



def factorial():
    """
    Генератор, возвращающий значения факториала последовательно.
    """
    n = 1
    fact = 1
    while True:
        yield fact
        n += 1
        fact *= n


factorial_gen = factorial()

print(next(factorial_gen))
print(next(factorial_gen))
print(next(factorial_gen))
print(next(factorial_gen))
print(next(factorial_gen))



