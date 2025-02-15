"""
Дан список пользователей след. формата: 
[{"name":"some_name", "login":"some_login", "password":"some_password" },
 ...
]

Отфильтровать используя функцию filter() список на предмет паролей 
которые менее 5 символов.

*Отфильтровать используя функцию filter() список на предмет валидных логинов. 
Валидный логин должен содержать только латинские буквы, цифры и черту подчеркивания. 
Каждому пользователю с плохим логином вывести текст 
"Уважаемый user_name, ваш логин user_login не является корректным."

"""



users = [
    {"name": "Alice Smith", "login": "alice_s", "password": "pas12"},
    {"name": "Bob Johnson", "login": "bob_j", "password": "secure_pass"},
    {"name": "Charlie Brown", "login": "charlie_b", "password": "brow"},
    {"name": "Diana Miller", "login": "diana_m", "password": "mill_pass"},
    {"name": "Eve Williams", "login": "eve_w", "password": "will"}
]


filt_5 = [i for i in filter(lambda user: (len(user["password"])) <= 5, users)]

print(filt_5)