"""
Написать декоратор который позволит не останавливать программу 
в случае если любая декорируемая функция выбрасывает ошибку, 
а выводить имя функции в которой произошла ошибка и информацию об ошибке в. 
Имя функции можно узнать использовав свойство __name__ ( print(func.__name__))

* сделать настраиваемы параметр который определяет печать в консоль или в файл
и если в файл передать название фала
"""

def error_handler(func):
    """Декоратор для обработки ошибок в функциях

    :param func: функция для обработки
    :return: обёрнутая функция
    """
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            print(f"Функция {func.__name__} выполнена успешно. Результат: {result}")
            return result
        except Exception as e:
            print(f"Ошибка в функции {func.__name__}: {type(e).__name__} - {str(e)}")
    return wrapper

@error_handler
def divide(a: float, b: float) -> float:
    """Выполняет деление a на b

    :param a: делимое
    :param b: делитель
    :return: результат деления
    """
    return a / b

@error_handler
def process_list(lst: list, index: int) -> float:
    """Сортирует список и умножает элемент на 2

    :param lst: список для обработки
    :param index: индекс элемента для умножения
    :return: результат умножения
    """
    return sorted(lst)[index] * 2

print("Результат 10 / 2:")
divide(10, 2)

print("\nПопытка деления на ноль:")
divide(10, 0)

print("\nОбработка списка:")
process_list([3, 1, 4, 1, 5], 2)

print("\nПопытка доступа к несуществующему индексу:")
process_list([1, 2, 3], 5)

print("\nПопытка обработки не-списка:")
process_list("not a list", 0)

print("\nПрограмма продолжает выполнение")
print("Выполняем дополнительные операции...")

for i in range(3):
    print(f"Дополнительная операция {i+1}")

print("Программа завершена успешно")
