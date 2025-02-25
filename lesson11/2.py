"""
Написать функцию hello, которая принимает 2 аргумента name и surname и
выводит принтом "Привет, {name} {surname}"

Написать декоратор log_decorator, который перед выполнением
функции печатает на экран строку, вида
Выполняеся функция <имя> с аргусентами <аргументы> 
После выполнения функции напечатать строку "<имя функции> - завершена"
"""


def log_decorator(log):
    """Декоратор для логирования вызовов функций

    Выводит информацию о вызове функции, её аргументах и завершении.

    :param func: декорируемая функция
    :return: обёрнутая функция с логированием
    """
    def wrapper(*args, **kwargs):
        args_str = ', '.join(map(str, args))
        kwargs_str = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        all_args = ', '.join(filter(bool, [args_str, kwargs_str]))
        print(f"Печатается функция {log.__name__}, с аргументами {all_args}")
        log(*args, **kwargs)
        print(f"{log.__name__} - завершена")
    return wrapper




@log_decorator
def hello(name: str, surname: str) -> None:
    """Выводит приветствие по имени и фамилии

    :param name: имя
    :param surname: фамилия
    """
    print(f"Привет, {name} {surname}")

    print(f"Привет, {name} {surname}")


hello("Kate", "Posledovich")
