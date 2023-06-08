money_on_count = 0
count_operations = 0
interest_rate = 1.5



def menu():
    print("1. Пополнить счет.\n"
          "2. Снять деньги со счета.\n"
          "3. Вывести баланс.\n"
          "4. Выйти.\n")


def add_money():
    global money_on_count
    print("Введите сумму, кратную 50$, которую Вы хотите положить на счет.")
    str_money = input()
    if str_money.isdigit():
        money = int(str_money)
        if check_sum(money):
            money_on_count += int(money)
            round(money_on_count, 2)
            print("Счет пополнен.\n")
        else:
            print("Необходимо ввести сумму кратную 50 и больше ноля.\n")
    else:
        print("Вы ввели не число. Попробуйте снова.\n")




def check_sum(money):
    if money > 0 and money % 50 == 0:
        return True
    else:
        return False


def withdraw_money():
    global interest_rate, money_on_count
    print("Введите сумму, кратную 50$, которую Вы хотите снять: ")
    str_withdraw = input()
    if str_withdraw.isdigit():
        withdraw = int(str_withdraw)
        if check_sum(withdraw):
            interest_money = withdraw * 1.5 / 100
            if interest_money < 30:
                interest_money = 30
            if interest_money > 600:
                interest_money = 600
            if withdraw + interest_money <= money_on_count:
                money_on_count -= withdraw
                money_on_count -= interest_money
                round(money_on_count, 2)
                print(f"Операция выполнена успешно с комиссией {round(interest_money, 2)}$\n")
            else:
                print("У Вас недостаточно средств на счете для осуществления операции.\n")
        else:
            print("Необходимо ввести сумму кратную 50 и больше ноля.\n")
    else:
        print("Вы ввели не число. Попробуйте снова.\n")




while True:
    if count_operations == 3:
        money_on_count -= money_on_count * 0.03
        round(money_on_count, 2)
        count_operations = 0
        print(f"Комиссия за выполнение 3х и более операций в размере {round(money_on_count * 0.03, 2)}$\n")

    menu()
    print("Выберите действие: ")
    user_choose = input()
    if user_choose == "1":
        if money_on_count > 5_000_000:
            money_on_count -= money_on_count * 0.05
            round(money_on_count, 2)
            print(f"Спиисание налога на богатство в размере {round(money_on_count * 0.05, 2)}$\n")
        add_money()
        count_operations += 1
    elif user_choose == "2":
        if money_on_count > 5_000_000:
            money_on_count -= money_on_count * 0.05
            round(money_on_count, 2)
            print(f"Спиисание налога на богатство в размере {round(money_on_count * 0.05, 2)}$")
        if money_on_count > 0:
            withdraw_money()
            count_operations += 1
        else:
            print(f"Баланс счета равен: {round(money_on_count, 2)}$.")
            print("Необходимо сначала положить деньги на счет.\n")
    elif user_choose == "3":
        print(f"Баланс счета равен: {round(money_on_count, 2)}$.\n")
    elif user_choose == "4":
        break
    else:
        print("Недопустимое значение. Попробуйте снова.\n")




