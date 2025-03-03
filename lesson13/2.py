"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).

Аксессоры реализоваться через property.
"""

from datetime import date

CURRENT_YEAR = date.today().year

class BookCard:
    def __init__(self, author, title, year):
        self.__author = author
        self.__title = title
        self.__year = year
    
    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise ValueError("неверный тип данных")
        self.__author = value

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("неверный тип данных")
        self.__title = value

    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, value):
        if  not isinstance(value, int):
            raise ValueError("неверный тип данных")
        if  value<=0 or value>=CURRENT_YEAR:
            raise ValueError ("вне временных рамок")
        self.__year = value
        

    def __lt__(self, other):
        return self.__year < other.__year

    def __le__(self, other):
        return self.__year <= other.__year

    def __eq__(self, other):
        return self.__year == other.__year

    def __ne__(self, other):
        return self.__year != other.__year

    def __gt__(self, other):
        return self.__year > other.__year

    def __ge__(self, other):
        return self.__year >= other.__year
    



book1 = BookCard("Лев Толстой", "Война и мир", 1869)
book2 = BookCard("Джордж Оруэлл", "1984", 1949)
book3 = BookCard("Харпер Ли", "Убить пересмешника", 1960)



print(f"Книга 1: {book1.author}, '{book1.title}', {book1.year}")
print(f"Книга 2: {book2.author}, '{book2.title}', {book2.year}")
print(f"Книга 3: {book3.author}, '{book3.title}', {book3.year}")



try:
    book1.year = 2050 
except ValueError as e:
    print(f"Ошибка при установке года: {e}")

try:
    book2.author = 123
except ValueError as e:
    print(f"Ошибка при установке автора: {e}")



books = [book1, book2, book3]
print("\nОтсортированные книги по году:")
print("\n".join(f"{book.year}: {book.title}" for book in sorted(books)))



print(f"\n{book1.title} старше {book2.title}? {book1 < book2}")
print(f"{book2.title} и {book3.title} изданы в один год? {book2 == book3}")






