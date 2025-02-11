'''
Запросить любое число. Заменить каждую цифру этого числа буквой, 
у которой номер в алфавите равен этой цифре. 
Например: 1352=aceb.
'''



import string

alphabet_string = string.ascii_lowercase
r_1 = range(1, len(alphabet_string) + 1)
dict_lett = dict(zip(r_1, alphabet_string))

num = input("Введите любое число: ")

try:
    if not num.isdigit():
        raise ValueError("Нужно ввести число.")

    sp = list(map(int, num))
    result_string = ""
    for i in sp:
        if i == 0:
            raise ValueError("Цифра 0 не имеет соответствия в алфавите.")
        if i not in dict_lett:
            raise ValueError(f"Цифра {i} не имеет соответствия в алфавите (1-{len(alphabet_string)}).")
        result_string += dict_lett[i]
    print(f"Введенное число {num} соответствует буквам {result_string}")

except ValueError as e:
    print(f"Ошибка: {e}")
