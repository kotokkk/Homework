'''
Запросить высоту елочки - число от 3 до 20. 
Напечатать на экране елочку где ее высота равна числу строк. 
Пример елочки из 4 строк:
   *
  ***
 *****
*******

'''



try:
    height = int(input("Введите высоту елки (от 3 до 20): "))

    if not 3 <= height <= 20:
        raise ValueError("Высота должна быть от 3 до 20.")

    for i in range(height):
        stars = "*" * (2 * i + 1)
        spaces = " " * (height - i - 1)
        print(spaces + stars)

except ValueError as e:
    print(f"Ошибка: {e}")
