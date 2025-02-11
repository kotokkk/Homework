"""
Написать функцию  которая принимает фамилию имя и отчество одной стройкой, 
а возвращает в виде краткого формата. 
Функция должна содержать необязательный параметр в виде логического значения 
# и в зависимости от него возвращала ФИО в двух следующих форматах:
#  -  Николаев И.С. 
#  -  И.С.Николаев


# """



def fio(name: str, way=True):
    try:
        parts = name.split()
        if not isinstance(name, str):
            raise TypeError('Нужно ввести строку')

        if len(parts) != 3:
            return 'Некорректный формат ФИО. Ожидается: Фамилия Имя Отчество'

        for part in parts:
            if any(char.isdigit() for char in part):
                raise ValueError('ФИО не должно содержать цифры')

        surname, first_name, patronymic = parts

        if way:
            return f"{surname} {first_name[0]}.{patronymic[0]}."
        else:
            return f"{first_name[0]}.{patronymic[0]}. {surname}"

    except TypeError as e:
        return f"Ошибка типа: {e}"
    except ValueError as e:
        return f"Ошибка значения: {e}"
    except IndexError:
        return "Ошибка: Некорректный формат ФИО. Ожидается: Фамилия Имя Отчество"
    except Exception as e:
        return f"Непредвиденная ошибка: {e}"

# Примеры использования
print(fio("Иванов Иван Иванович"))
print(fio("Иванов Иван Иванович", way=False))
print(fio("Иванов"))
print(fio(123))
print(fio("Иванов Иван1 Иванович"))
