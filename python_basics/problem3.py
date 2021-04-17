from datetime import datetime as dt
import locale


def my_date_is_between(my_date, my_date_from, my_date_to):
    # датам устанавливается 2000 год (заведомо високосный), чтобы корректно обрабатывалось 29 февраля
    d, date_from, date_to = [dt.strptime(_d + ' 2000', '%d %B %Y') for _d in [my_date, my_date_from, my_date_to]]
    return date_from <= d <= date_to


locale.setlocale(locale.LC_TIME, "ru_RU")

print('Введите день:')
day = int(input())
# использование стандартного модификатора формата %B для месяца делает ввод регистронезависимым
print('Введите месяц:')
month = input()
date = f'{day} {month}'

if my_date_is_between(date, '22 Декабрь', '31 Декабрь') or my_date_is_between(date, '1 Январь', '19 Январь'):
    result = 'Козерог'
elif my_date_is_between(date, '20 Январь', '18 Февраль'):
    result = 'Водолей'
elif my_date_is_between(date, '19 Февраль', '20 Март'):
    result = 'Рыбы'
elif my_date_is_between(date, '21 Март', '19 Апрель'):
    result = 'Овен'
elif my_date_is_between(date, '20 Апрель', '20 Май'):
    result = 'Телец'
elif my_date_is_between(date, '21 Май', '20 Июнь'):
    result = 'Близнецы'
elif my_date_is_between(date, '21 Июнь', '22 Июль'):
    result = 'Рак'
elif my_date_is_between(date, '23 Июль', '22 Август'):
    result = 'Лев'
elif my_date_is_between(date, '23 Август', '22 Сентябрь'):
    result = 'Дева'
elif my_date_is_between(date, '23 Сентябрь', '22 Октябрь'):
    result = 'Весы'
elif my_date_is_between(date, '23 Октябрь', '21 Ноябрь'):
    result = 'Скорпион'
elif my_date_is_between(date, '22 Ноябрь', '21 Декабрь'):
    result = 'Стрелец'
else:
    raise Exception('Неизвестная ошибка!')

print(f'Ваш знак зодиака: {result}')
