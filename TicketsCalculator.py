# 1. В начале у пользователя запрашивается количество билетов, которые он хочет приобрести на мероприятие.
# 2. Далее для каждого билета запрашивается возраст посетителя, в соответствии со значением которого выбирается
# стоимость:
# Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно.
# От 18 до 25 лет — 990 руб.
# От 25 лет — полная стоимость 1390 руб.
# 3. В результате программы выводится сумма к оплате. При этом, если человек регистрирует больше трёх человек на
# конференцию, то дополнительно получает 10% скидку на полную стоимость заказа.


# Получение числа билетов от пользователя и исключение ошибки, если (str).
running = True
while running:

    # Сумма стоимости билетов
    Summary = []

    try:
        print('При заказе от 3-х билетов будет начислена скидка в размере 10% от стоимости всех билетов.')
        UserInputNumberOfTickets = int(input('Введите колличество билетов для покупки: '))
        if UserInputNumberOfTickets >= 3:
            print('Сумма билетов будет рассчитана со скидкой')
            DiscountPrice = [0, 891, 1251]
        else:
            DiscountPrice = [0, 990, 1390]

    except ValueError as e:
        print('Для ввода допустимы только целые числа!')

    else:

        # Создание списка из UserInputNumberOfTickets
        ListOfTickets = list(range(UserInputNumberOfTickets))

        # Итерация по введёным билетам по возрасту, получение цен.
        for UserInputNumberOfTickets in ListOfTickets:
            Age = int(input('Введите возраст для билета: '))

            # до 18 лет - Бесплатно.
            if Age <= 17:
                print('Стоимость билета =', DiscountPrice[0], 'руб.')
                Summary.append(DiscountPrice[0])

            # От 18 до 25 лет — 990 руб.
            elif 18 <= Age < 25:
                print('Стоимость билета =', DiscountPrice[1], 'руб.')
                Summary.append(DiscountPrice[1])

            # От 25 лет — 1390 руб.
            else:
                print('Стоимость билета =', DiscountPrice[2], 'руб.')
                Summary.append(DiscountPrice[2])

        # Печать суммы стоимости билетов.
        print('Итоговая стоимость билетов = ', (sum(Summary)))
        break
        
# Выполнил Живилов Игорь, QAP-94.