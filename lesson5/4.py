'''
Буква "a" стоит 10 очков, "b" - 20, "c" - 30, "d" - 40
Запросить кодовою фразу из пяти символов используя только a, b, c, d.
Вывести на экран общее количество очков введенной фразы.

'''
import re

letters = {"a":10, "b":20, "c":30, "d":40}

phrase = input("Введите фразу из пяти символов используя только a, b, c, d: ")

a = re.split(r'[,\s]+', phrase)

total_sum = sum(letters[char] * a.count(char) for char in letters)

print(f"Общее количество очков введенной фразы: {total_sum}")












# это я сразу написала буквально дословно что и как делаю, потом искала способы сокртить этот код, получилось то что вверху

# g = letters[a[0]]
# d = a.count("a")
# h = g*d


# t = letters[a[1]]
# y = a.count("b")
# u = t*y

# i = letters[a[2]]
# o = a.count("c")
# p = i*o

# l = letters[a[3]]
# k = a.count("d")
# j = l*k

# list = [h, u, p, j]
# sm = sum(list)


# print(f"Общее количество очков введенной фразы: {sm}")