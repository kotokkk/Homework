'''
Дан список [1,2,3,4,5,6,7,8,9]. Создать 3 копии этого списка 
и с каждой выполнить след действия:
    - возвести каждый элемент во 2ю степень
    - прибавить 3 к каждому элементу значение которого является четным 
    - элементы значения которого является 
            четными - умножить на 2 
            нечетным - умножить на 3

Использовать map и lambda.
'''



list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def elevation(x):
    """Возводит число в квадрат."""
    return x ** 2

def calculation(x):
    """Прибавляет 3 к четным числам."""
    return x + 3 if x % 2 == 0 else x
    
def even_odd(x):
    """Умножает четные числа на 2 и нечетные на 3. """
    return x * 2 if x % 2 == 0 else x * 3


# list_squared = list(map(elevation, list1.copy()))       
# list_added_even = list(map(calculation, list1.copy())) 
# list_even_odd = list(map(even_odd, list1.copy()))     


print(f"{list1} Исходный список")
print(f"{list(map(elevation, list1.copy()))} Список после возведения в квадрат")
print(f"{list(map(calculation, list1.copy()))} Список после прибавления 3 к четным")
print(f"{list(map(even_odd, list1.copy()))} Список после умножения четных на 2 и нечетных на 3")
