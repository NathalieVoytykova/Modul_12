money = float(input("Введите сумму вклада: "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
banks = list(per_cent.keys())
per_cent = list(per_cent.values())
deposit = list()
deposit.append(int(money/100*float(per_cent[0])))
deposit.append(int(money/100*float(per_cent[1])))
deposit.append(int(money/100*float(per_cent[2])))
deposit.append(int(money/100*float(per_cent[3])))
print(f'\nДоход по депозиту:\n банк {banks[0]} - {deposit[0]} рублей'
      f'\n банк {banks[1]} - {deposit[1]} рублей'
      f'\n банк {banks[2]} - {deposit[2]} рублей'
      f'\n банк {banks[3]} - {deposit[3]} рублей')
max_deposit = max(deposit)
print("Максимальный доход по депозиту: {} рублей".format(max_deposit))
