'''
Запросить любое число. Заменить каждую цифру этого числа буквой, 
у которой номер в алфавите равен этой цифре. 
Например: 1352=aceb.
'''

# import string

# alphabet_string = string.ascii_lowercase

# r_1 = range(1, len(alphabet_string) +1)

# dict_lett = dict(zip(r_1,alphabet_string))

# num = input("Введите любое число: ")

# if num.isdigit():
#     sp = list(map(int, num))
#     for i in sp:
#         print(dict_lett[i], end ="")
# else:
#     print("Ошибка.Нужно ввести число")

   
   
   
   
   
# import string

# alphabet_string = string.ascii_lowercase

# r_1 = range(1, len(alphabet_string) +1)

# dict_lett = dict(zip(r_1,alphabet_string))

# num = input("Введите любое число: ")

# if num.isdigit() and any(char in string.punctuation for char in num) != True:
#     sp = list(map(int, num))
#     for i in sp:
#         print(f"Введенное число {num} соответствует буквам {dict_lett[i]}", end ="")
# else:
#     print("Ошибка.Нужно ввести число. Нельзя использовать пунктуацию")

   
   
   
   
   
   
   
   
import string

alphabet = string.ascii_lowercase
letter_dict = dict(zip(range(1, len(alphabet) + 1), alphabet))

num_str = input("Введите число: ")

if num_str.isdigit() and all(c not in string.punctuation for c in num_str):
  result = ''.join(letter_dict.get(int(digit), '') for digit in num_str)
  print(result)
else:
  print("Ошибка: Введите целое число без знаков препинания.")
