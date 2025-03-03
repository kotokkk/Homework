"""
Создать класс Student.


Определить атрибуты:
    - surname - фамилия
    - name - имя
    - group - номер группы
    - grads - список оценок

Определить методы:
    - инициализатор __init__
    - Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
    студентов по среднему баллу
    - метод add_grade - добавляет в список оценок одну или несколько оценок от 1 до 10
    - метод average_grade -считает и возвращает среднюю оценку ученика

Создать список из 5 студентов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 8
"""


class Student:
    def __init__(self, surname, name, group, grades=None):
        self.surname = surname
        self.name = name
        self.group = group
        self.grades = grades if grades is not None else []

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()

    def add_grade(self, *args: int):
        for grade in args:
            if not 1 <= grade <= 10:
                raise ValueError(f"Некорректная оценка: {grade}. Оценка должна быть от 1 до 10.")
        self.grades.append(grade)
        

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __repr__(self):
        return (
            f"Student(surname='{self.surname}', name='{self.name}', "
            f"group='{self.group}', average_grade={self.average_grade():.2f})"
        )



students = [
    Student("Иванов", "Иван", "10A", [8, 9, 7, 10]),
    Student("Петров", "Петр", "10Б", [7, 6, 8, 9]),
    Student("Сидоров", "Сидор", "10А", [9, 10, 9, 8]),
    Student("Смирнов", "Алексей", "10В", [6, 7, 5, 8]),
]




print("Сортировка по возрастанию:")
for student in sorted(students):
    print(student)

print("\nСортировка по убыванию:")
for student in sorted(students, reverse=True):
    print(student)

print("\nСтуденты со средним баллом больше 8:")
for student in students:
    if student.average_grade() > 8:
        print(student)