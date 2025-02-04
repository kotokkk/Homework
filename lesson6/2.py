'''
запросить у пользователя логин пароль и возраст
вывести доступ разрешен:
    логин:admin   пароль:123456    возраст: любой    
    логин:vasya   пароль: vas123   возраст: менее 60
    логин:guest   пароль: любой    возраст:более 18
    
в остальных случаях - "доступ запрещен".

'''

login = input("Enter login: ").lower()
password = (input("Enter password: "))
age_1 = input("Enter age: ")

if age_1.isdigit():
    age = int(age_1)
    if login == "admin" and password == "123456" and age in range(1,110):
        print("Доступ разрешен")
    elif login == "vasya" and password == "vas123" and age <60:
        print("Доступ разрешен")
    elif login == "guest" and age>18:
        print("Доступ разрешен")
    else:
        print("Доступ запрещен")
else:
    print("Доступ запрещен")