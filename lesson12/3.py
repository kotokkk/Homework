"""

Описать класс Counter, реализующий целочисленный счетчик.
который может увеличивать или уменьшать свое значение (атрибут value)
на единицу в заданном диапазоне.

Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.

Определить атрибуты(свойства):
    - value - текущее значение счетчика
    ...

Определить методы:
    - инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
    - increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
    - decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
    - reset, сбрасывает значение счетчика на стартовое    
    - метод __iter__
    - метод __next__
    
    * - stat, возвращает среднее количество изменений счетчика в секунду

"""



class Counter:
    def __init__(self, start=0, min_value=None, max_value=None):
        self.start = start
        self.value = start
        self.min_value = min_value
        self.max_value = max_value

    def increase(self, num=1):
        new_value = self.value + num
        if self.max_value is not None:
            self.value = min(new_value, self.max_value)
        else:
            self.value = new_value

    def decrease(self, num=1):
        new_value = self.value - num
        if self.min_value is not None:
            self.value = max(new_value, self.min_value)
        else:
            self.value = new_value

    def reset(self):
        self.value = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.max_value is not None and self.value >= self.max_value:
            raise StopIteration
        self.increase()
        return self.value

    def __str__(self):
        return str(self.value)



if __name__ == "__main__":
    c = Counter(5, 0, 10)
    print(f"Начальное значение: {c}")
    c.increase(3)
    print(f"После увеличения на 3: {c}")
    c.decrease(2)
    print(f"После уменьшения на 2: {c}")
    c.reset()
    print(f"После сброса: {c}")
    print("Итерация:", [i for i in c])