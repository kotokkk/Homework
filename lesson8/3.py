'''
Написать функцию, которая вычисляет  факториал переданного в нее числа без рекурсии.

'''



def factorial_iterative(n):
    if n < 0:
        return None  
    elif n == 0:
        return 1    
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
# пример использования
num = 5
fact = factorial_iterative(num)
print(f"Факториал числа {num} равен {fact}") 
