'''
Дан произвольный список из 5 элементов. 
     - Поменять местами 1ый и последний элемент
     - удалить и вывести на печать третий элемент
'''

list_dif = [1, 2, 3, 4, "Hello", 5, False]

a = list_dif[0]
list_dif[0] = list_dif[6]
list_dif[6] = a

print("Измененный список:", list_dif)

b = list_dif.pop(2)

print("Список без удаленного элемента:", list_dif, "\nУдаленный элемент:", b)