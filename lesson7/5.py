'''

Дан списк:
['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']
Для каждого элемента в списке 
    - вывести на экран сначала номер элемента 
    - сам элемент 
    - символ данного элемента, соответствующий номеру его позиции в списке. 
Образец:
1 - qwertyu - q
2 - asdfggh - s
3 - zxcvbnm - c
и так далее...


'''

l = ['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']


for index, item in enumerate(l):
    print(f"{index+1} - {item} - {item[index]}")
