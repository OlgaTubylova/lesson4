# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.

def apply_wealth_tax(balance):
    if balance > 5_000_000:
        tax = balance * 0.1
        balance -= tax
        print(f"Вычтен налог на богатство 10%: {tax}")
    return balance

def deposit(balance, amount, transactions):
    if amount % 50 == 0:
        balance += amount
        transactions.append(f"Пополнение: +{amount}")
        return balance, True
    else:
        print("Ошибка: сумма должна быть кратна 50")
        return balance, False

def withdraw(balance, amount, transactions):
    if amount % 50 != 0:
        print("Ошибка: сумма должна быть кратна 50")
        return balance, False
    
    if amount > balance:
        print("Ошибка: недостаточно средств")
        return balance, False
    
    commission = max(30, min(600, amount * 0.015))
    total_withdraw = amount + commission
    
    if total_withdraw > balance:
        print("Ошибка: недостаточно средств с учетом комиссии")
        return balance, False
    
    balance -= total_withdraw
    transactions.append(f"Снятие: -{amount}, комиссия: -{commission}")
    return balance, True

def apply_bonus(balance, operation_count):
    if operation_count % 3 == 0:
        bonus = balance * 0.03
        balance += bonus
        print(f"Начислен бонус 3%: {bonus}")
    return balance

def atm():
    balance = 0
    transactions = []
    operation_count = 0
    
    while True:
        balance = apply_wealth_tax(balance)
        action = input("Выберите действие (пополнить, снять, выйти): ").strip().lower()
        
        if action == "пополнить":
            try:
                amount = int(input("Введите сумму пополнения: "))
                balance, success = deposit(balance, amount, transactions)
                if success:
                    operation_count += 1
                    balance = apply_bonus(balance, operation_count)
            except ValueError:
                print("Ошибка: введите корректное число")
        
        elif action == "снять":
            try:
                amount = int(input("Введите сумму снятия: "))
                balance, success = withdraw(balance, amount, transactions)
                if success:
                    operation_count += 1
                    balance = apply_bonus(balance, operation_count)
            except ValueError:
                print("Ошибка: введите корректное число")
        
        elif action == "выйти":
            print("История операций:")
            for transaction in transactions:
                print(transaction)
            print(f"До свидания! Итоговый баланс: {balance}")
            break
        
        else:
            print("Ошибка: неверное действие")
        
        print(f"Текущий баланс: {balance}")

if __name__ == "__main__":
    atm()





# def atm():
#     money = 0  # Начальная сумма
#     counter = 0  # Счетчик операций

#     while True:
#         # Проверяем налог на богатство перед любой операцией
#         if money > 5000000:
#             money -= money * 0.1
#             print("Вычтен налог на богатство 10%")

#         action = input('Выберите действие: пополнить, снять, выйти: ').strip().lower()

#         if action == 'пополнить':
#             amount = int(input('Введите сумму: '))
#             if amount % 50 == 0:
#                 money += amount
#                 counter += 1

#                 # Бонус за каждую третью операцию
#                 if counter % 3 == 0:
#                     money += money * 0.03
#                     print("Начислен бонус 3% за третью операцию!")

#                 print(f"Баланс: {money}")
#             else:
#                 print('Ошибка: сумма должна быть кратна 50')

#         elif action == 'снять':
#             amount = int(input('Введите сумму: '))
#             if amount % 50 == 0:
#                 commission = max(30, min(600, amount * 0.015))  # Рассчитываем комиссию (1.5%)
#                 total_withdraw = amount + commission

#                 if total_withdraw <= money:
#                     money -= total_withdraw
#                     counter += 1

#                     # Бонус за каждую третью операцию
#                     if counter % 3 == 0:
#                         money += money * 0.03
#                         print("Начислен бонус 3% за третью операцию!")

#                     print(f"Баланс: {money}")
#                 else:
#                     print('Ошибка: недостаточно средств')

#             else:
#                 print('Ошибка: сумма должна быть кратна 50')

#         elif action == 'выйти':
#             print(f"До свидания! Итоговый баланс: {money}")
#             break

#         else:
#             print('Ошибка: неверное действие')

# if __name__ == '__main__':
#     atm()
