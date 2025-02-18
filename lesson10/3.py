"""
Написать функцию которая принимает строку в которой есть 
круглые скобки и возвращает True или False анализируя все ли скобки 
являются закрытыми и расставлены в правильном порядке.
Примеры:
    (()()) -> True
    (()()() -> False
    (hello(2)ver()(33)python) -> True
    (hello(2()ver(33)python)) -> True
    (hello(2()ver(33)python) -> False

"""


def are_par_balanced(s):
    """
    Проверяет, правильно ли расставлены круглые скобки в строке.

    Аргументы:
        s (str): Строка, содержащая символы, включая круглые скобки.

    Возвращает:
        bool: True, если все открывающие скобки имеют соответствующие закрывающие 
              и расставлены в правильном порядке; иначе False.
    """

    stack = 0
    for char in s:
        if char == '(':
            stack += 1
        elif char == ')':
            stack -= 1
            if stack < 0:
                return False
    return stack == 0


print(are_par_balanced("(()())")) 
print(are_par_balanced("(()()()")) 
print(are_par_balanced("(hello(2)ver()(33)python)")) 
print(are_par_balanced("(hello(2()ver(33)python))")) 
print(are_par_balanced("(hello(2()ver(33)python)")) 
