"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
а возвращает список из Yes или No для каждого элемента, 
Yes - если число уже встречалось и No, если нет
[1,2,3,1,4] => [no, no, no, yes, no]

если в списке не все целые числа вернуть False.

"""


def yes_or_no(numbers):
    if not all(isinstance(num, int) for num in numbers):
        return False

    seen = set()
    result = []

    for num in numbers:
        if num in seen:
            result.append("Yes")
        else:
            result.append("No")
            seen.add(num)

    return result

# пример использования
numbers = [1, 2, 3, 1, 4]
result = yes_or_no(numbers)
print(result)
# пример использования
numbers2 = [1, 2, 3, 1, "4"]
result2 = yes_or_no(numbers2)
print(result2) 
