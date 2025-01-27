purchase_price = float(input("Введите цену закупки телефона: "))

selling_price = purchase_price * 1.3

discount_5 = selling_price * 0.95
discount_10 = selling_price * 0.90
discount_15 = selling_price * 0.85

print(f"Цена продажи: {selling_price:.0f} руб.")
print(f"Цена продажи со скидкой 5%: {discount_5:.0f} руб.")
print(f"Цена продажи со скидкой 10%: {discount_10:.0f} руб.")
print(f"Цена продажи со скидкой 15%: {discount_15:.0f} руб.")
