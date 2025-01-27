number = int(input("Введите число: "))

thousands = number // 1000         
hundreds = (number % 1000) // 100 
tens = (number % 100) // 10        
units = number % 10                 

print(f"Тысяч - {thousands}")
print(f"Сотен - {hundreds}")
print(f"Десятков - {tens}")
print(f"Единиц - {units}")
