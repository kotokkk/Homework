'''
Запросить по очереди у пользователя 5 имен. Добавить все в список. 
Отсортировать. 
Вывести на экран.
Вывести True при наличии в списке имени 'Вася'
'''


user_data = [input(f"Введите имя {i+1}: ") for i in range(5)]

user_data.sort()

print("Отсортированный список: ", user_data, "\nИмя 'Вася' находится в списке? Ответ: ", "Вася" in user_data)


