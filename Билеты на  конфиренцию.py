tickets = int(input('Введите количество необходимых билетов:'))
person = tickets
cash = 0
while person != 0:
    age_for_ticket = int(input(f'Для какого возраста билет № {person}'))
    if age_for_ticket < 18:
        print('Билет бесплатный')
    elif 25 > age_for_ticket >= 18:
        cash += 990
        print('Стоимость билета: 990 руб.')
    else:
        cash += 1390
        print('Стоимость билета: 1390 руб.')
    person -= 1
if tickets > 3:
    sale = cash - ((cash/100)*10)
    print(f'Сумма к оплате {sale} руб., применена скадка 10% за покупку более 3 билетов')