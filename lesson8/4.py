'''

Написать функцию, которая возвращает любое число в виде денежной величины 
с разделителями групп разрядов в качестве пробела и валютой в конце. 
Денежная величина всегда должна содержать количество копеек в виде дух 
знаков после точки, даже если исходное число целое. 
*Нельзя использовать форматную строку.
Например: 1234567 -> "1 234 567.00 руб."

с помощью try перехватить возможные ошибки.
'''



def format_as_currency(number):
    try:
        number = float(number) 

        rubles = int(number)
        kopecks = int(round((number - rubles) * 100)) 

        kopecks_str = str(kopecks).zfill(2)

        rubles_str = ""
        rubles_list = list(str(rubles))
        rubles_list.reverse() 
        for i, digit in enumerate(rubles_list):
            rubles_str += digit
            if (i + 1) % 3 == 0 and i != len(rubles_list) - 1:
                rubles_str += " "
        rubles_str = rubles_str[::-1]

        return f"{rubles_str}.{kopecks_str} руб."

    except ValueError:
        print("Ошибка: Введено некорректное число.")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

# Примеры использования
print(format_as_currency(1234567))      
print(format_as_currency(1234.567))      
print(format_as_currency(123))            
print(format_as_currency("abc"))        
print(format_as_currency(123456789.99999))
