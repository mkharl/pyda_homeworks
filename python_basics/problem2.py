year = 2020
print(f"{'Високосный' if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else 'Обычный'} год")
