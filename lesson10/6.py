"""
Написать генератор triangular_numbers, который возвращает подряд 
треугольные числа

Формула:
Tn = 1 / 2 * n * (n + 1)

Например:
tn_gen = triangular_numbers()

next(tn_gen) -> 1
next(tn_gen) -> 3
next(tn_gen) -> 6
next(tn_gen) -> 10
next(tn_gen) -> 15
next(tn_gen) -> 21
"""





def triangular_numbers():
    """
    Генератор треугольных чисел.

    Бесконечно генерирует последовательность треугольных чисел, начиная с 1.
    Треугольные числа - это сумма натуральных чисел от 1 до n, где n - номер числа.

    Каждое треугольное число вычисляется по формуле: Tn = n * (n + 1) / 2,
    и возвращается как целое число.

    Возвращает:
        int: Значение текущего треугольного числа.
    """

    n = 0
    while True:
        n += 1
        c = int(1 / 2 * n * (n + 1))
        yield c

tn_gen = triangular_numbers()

print(next(tn_gen))
print(next(tn_gen))
print(next(tn_gen))
print(next(tn_gen)) 
print(next(tn_gen)) 
print(next(tn_gen)) 