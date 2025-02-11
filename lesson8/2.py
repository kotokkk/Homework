'''
Написать функцию которая принимает 2 стороны прямоугольника 
и возвращает либо площадь либо периметр в зависимости от дополнительного параметра.

'''

# без проверки на ошибки

def count_rec(a: float, b: float, calculate_area=True):
    if calculate_area:
        return a * b
    return (a + b) * 2
# пример использования
print(count_rec(5, 6, False))





# с проверкой на возможные ошибки

def rect(a, b, calculate_area=True):
  try:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
      raise TypeError("Стороны должны быть числами")
    if a <= 0 or b <= 0:
      raise ValueError("Стороны должны быть положительными")

    if calculate_area:
      return a * b
    return 2 * (a + b)
  except Exception as e:
    print("Ошибка:", e)
    return None 
# пример использования
print(rect(5, 10))
print(rect(5, 10, False))
print(rect("a", 10))
