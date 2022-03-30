import sys

number_tickets = int(input('Кол-во билетов '))
if number_tickets < 0:
    raise ValueError('Не может быть столько билетов!')
price_tickets = 0
age = int(input('Возраст '))
if age > 100 or age <= 0:
    raise ValueError('Не может быть столько лет!')
if number_tickets > 0 and age < 18:
    print('Проходите беслатно!')
    sys.exit()
for i in range(number_tickets):

    #i += 1

    if 18 <= age and age < 25:
        price_tickets += 990

    if age >= 25:
        price_tickets += 1390

if number_tickets > 3:
    price_tickets = price_tickets * 0.9
    print(f"Стоимость билетов с 10% скидкой для {number_tickets} человек: ", int(price_tickets))



else:
    print("Сумма к оплате:", int(price_tickets))
