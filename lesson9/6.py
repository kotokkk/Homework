"""
Дан словарь наблюдения за температурой 
{"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}. 
Отсортировать словарь по температуре в порядке возрастания и обратно.

"""

d1 = {"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}

sort_d1 = {key:value for key, value in sorted(d1.items(), key=lambda i: i[1])}
revers_sort_d1 = {key:value for key, value in sorted(d1.items(), key=lambda i: i[1], reverse=True)}


print(f"""В порядке возрастания: {sort_d1}
В порядке убывания: {revers_sort_d1}
""")
