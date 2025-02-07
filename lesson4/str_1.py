'''
Программа должна запросить любую фразу и вывести на экран :
     - количество символов в данной фразе.
     - количество слов  в данной фразе. 
            Словом может считаться любой набор символов разделенный от 
            других пробелом и количеством символов больше или равных 1.
     -* количество гласных в данной фразе. Нельзя использовать if и for.

'''

info = input("Введите фразу: ")

symb = len(info)

a = info.split()
symb_2 = len(a)

vowels = "ауоыиеэяюёеАУОЫИЭЯЮЁЕ"
vowel_count = sum(map(lambda x: x in vowels, info))

print("Количество слов:", symb_2)
print("Количество символов:", symb)
print("Количество гласных:", vowel_count)