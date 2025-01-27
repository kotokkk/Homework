# Вывод времени с использованием форматной строки

total_seconds = int(input("Введите количество секунд: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")






# Вывод времени без использования форматной строки

# total_seconds = int(input("Введите количество секунд: "))

# hours = total_seconds // 3600
# minutes = (total_seconds % 3600) // 60
# seconds = total_seconds % 60

# print("{:02}:{:02}:{:02}".format(hours, minutes, seconds))
