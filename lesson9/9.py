"""
Написать функцию dict_from_args, которая принимает неограниченное
количество позиционных аргументов и неограниченное количество аргументов
ключевых-слов.

Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
нет, то кинуть ошибку TypeError("Все позиционные аргументы должны быть целыми").

Если все именованные аргументы - ключевые слова являются строками, то найти максимальную
длину слова. Если нет, то кинуть ошибку TypeError("Все аргументы - ключевые
слова должны быть строками").

Функция должна вернуть словарь, вида:
{
    "args_sum": 13,
    "kwargs_max_len": 7
}
"""

def dict_from_args(*args, **kwargs):
    try:
        sum1 = 0
        for num in args:
            if not isinstance(num, int):
                raise TypeError("Все позиционные аргументы должны быть целыми") 
            sum1 += num
        max_len = 0
        for key, value in kwargs.items():
            if not isinstance(value, str):
                raise TypeError("Все аргументы - ключевые слова должны быть строками")
            max_len = max(max_len, len(value))
        return {
        "args_sum": sum1,
        "kwargs_max_len": max_len
        }

    except TypeError as e:
        return f"Ошибка типа: {e}"
        
#Примеры использования   
result = dict_from_args(1, 2, 3, 4, 5, name="Alice", city="New York", job="Developer") 
print(result)


result = dict_from_args(1, 2, 3, "четыре", 5, name="Alice", city="New York", job="Developer") 
print(result)


result = dict_from_args(1, 2, 3, 4, 5, name="Alice", city=123, job="Developer") 
print(result)













#Через all()

def dict_from_args(*args, **kwargs):
    if not all(isinstance(num, int) for num in args):
        raise TypeError("Все позиционные аргументы должны быть целыми")

    if not all(isinstance(value, str) for value in kwargs.values()):
        raise TypeError("Все аргументы - ключевые слова должны быть строками")

    return {
        "args_sum": sum(args), 
        "kwargs_max_len": max(len(value) for value in kwargs.values())
    }

# Примеры использования
try:
    result = dict_from_args(1, 2, 3, 4, 5, name="Alice", city="New York", job="Developer")
    print(result)
except TypeError as e:
    print(f"Ошибка типа: {e}")

try:
    result = dict_from_args(1, 2, 3, "четыре", name="Alice", city="New York")
    print(result)
except TypeError as e:
    print(f"Ошибка типа: {e}")

try:
    result = dict_from_args(1, 2, 3, name="Alice", city=123)
    print(result)
except TypeError as e:
    print(f"Ошибка типа: {e}")
