from decimal import Decimal

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
d = input('Введите сумму:')
money = Decimal(d)
deposit = []

for bank, rate in per_cent.items():
    interest = money * Decimal(str(rate)) / Decimal('100')
    deposit.append(str(bank))
    deposit.append(str(interest))

print("Депозиты:", deposit)

max_deposit = max(deposit)
print("Максимальная сумма, которую вы можете заработать:", max_deposit)
