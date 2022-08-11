Tickets = int(input('Введите колличество билетов, которые вы желаете приобрести :'))
Years = int(input('Введите возраст:'))
prise_1 = 990
prise_2 = 1390
sale_1 = (prise_1 * Tickets)-((prise_1 * Tickets) / 100 * 10)
sale_2 = (prise_2 * Tickets)-((prise_2 * Tickets) / 100 * 10)
if Years < 18:
    print('Проход на конференцию бесплатный')
elif 18 <= Years < 25:
    if Tickets > 3:
        print(f'Стоимость билетов, со скидкой, составит:{sale_1} руб.')
    print(f'Стоимость билетов: {prise_1 * Tickets} руб.' )
elif Years >= 25:
    if Tickets > 3:
        print(f'Стоимость билетов, со скидкой, составит:{sale_2} руб.')
    print(f'Стоимость билетов: {prise_2 * Tickets} руб.')
