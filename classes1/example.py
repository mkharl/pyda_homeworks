from exchange import Rate
from designer import Designer

# Задание 1
print(Rate.greatest_currency())

# Задание 2
r1 = Rate(format_='value', diff=True)
r2 = Rate(format_='value', diff=False)
r3 = Rate(format_='full', diff=True)

print(r1.azn(), r2.eur(), r3.usd())

# Задание 3
# честно говоря, я не уверен, что я понял задание :(
staff1 = Designer('Zaha Hadid')
for i in range(20):
    staff1.check_if_it_is_time_for_upgrade()
