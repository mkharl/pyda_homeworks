number = 123321
print(f"{'Счастливый' if sum(map(int, str(number)[:3])) == sum(map(int, str(number)[-3:])) else 'Несчастливый'} билет")
