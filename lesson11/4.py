'''
открыть и обработать файл students_grades.txt
собрать все данные в словарь ниже приведенного формата
записать в файл "excellent_students.txt" по 1 ученику из класса с наибольшим балом
{
    "9A":[
        {'fio':'fio', 
         'objects':{
            'mathematics':[4, 9, 7],
            'physics':[8, 9, 8, 6],
            ...:...
            }
        },
        ...        
    ],
    "9Б":[
        ...
    ]
}

'''


import re
from pprint import pprint

def get_students(filename: str) -> dict:
    """
    Читает данные о студентах из файла и создает структурированный словарь.

    :param filename: имя файла с данными о студентах
    :return: словарь с информацией о студентах, сгруппированной по классам
    """
    grades = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(', ', 2)
            fio = parts[0]
            class_name = parts[1]
            subjects = parts[2].split('), ')

            if class_name not in grades:
                grades[class_name] = []

            student = {"fio": fio, "objects": {}}

            for subject in subjects:
                match = re.match(r'(.*?)\s*\((.*?)\)?$', subject)
                if match:
                    subject_name, grades_str = match.groups()
                    subject_grades = [int(grade.strip()) for grade in grades_str.split(',')]
                    student['objects'][subject_name] = subject_grades

            grades[class_name].append(student)

    return grades

def find_excellent_students(grades_dict: dict) -> dict:
    """
    Находит лучшего ученика в каждом классе на основе суммы всех оценок.

    :param grades_dict: словарь с информацией о студентах и их оценках
    :return: словарь с именами лучших учеников для каждого класса
    """
    excellent_students = {}

    for class_name, students in grades_dict.items():
        if students:
            best_student = max(
                students,
                key=lambda s: sum(sum(grades) for grades in s['objects'].values())
            )
            excellent_students[class_name] = best_student['fio']
        else:
            excellent_students[class_name] = None

    return excellent_students


grades_dict = get_students('students_grades.txt')

excellent_students = find_excellent_students(grades_dict)


with open('excellent_students.txt', 'w', encoding='utf-8') as file:
    for class_name, student in excellent_students.items():
        file.write(f"{class_name}: {student}\n")


pprint(grades_dict)
