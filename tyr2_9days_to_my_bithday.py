argum = sys.argv[1:]
if len(argum) == 0:
    print('-help- Помощь')
if 'help' in argum:
    if len(argum) == 1:
        print('''Доступные команды:
-reg- Регистрация
-login- Авторизация
-delete_account- Удаление аккаунта
-list- Список продуктов
-buy- <name> <count> Покупка товара
-addbalance- <value> Пополнение кошелька
-status- <index> Информация о пользователе по индексу
-myself- Вывод совершенных покупок

Используйте help для данных комманд для получения дополнительной информации.
''')
    elif len(argum) == 2:
        if argum[0] == 'reg' and argum[1] == 'help':
            print('''Регистрация в системе (логин и пароль)''')
        elif argum[0] == 'login' and argum[1] == 'help':
            print('Авторизация через логин и пароль')
        elif argum[0] == 'logout' and argum[1] == 'help':
            print('Выход из учетной записи')
        elif argum[0] == 'delete_account' and argum[1] == 'help':
            print('Удаление учётной записи с просьбой об подтверждении действия.')
        elif argum[0] == 'list' and argum[1] == 'help':
            print('Вывод всех доступных покупок их стоимости и оставшегося количества')
        elif argum[0] == 'buy' and argum[1] == 'help':
            print('''Покупка товара (name) в количестве.
Аргументы:
<name> - название продукта
<count> - количество
''')
        elif argum[0] == 'addbalance' and argum[1] == 'help':
            print('''Пополнение счета авторизованного пользователя на определенную сумму
Аргументы:
<value> - Количество денег
''')
        elif argum[0] == 'status' and argum[1] == 'help':
            print('Информация об авторизированном пользователе (баланс ,количество покупок и их стоимость)')
        elif argum[0] == 'myself' and argum[1] == 'help':
            print('Вывод совершённых покупок(наименование товара, количество, общ. Стоимость)')    
    exit()
del argum
