import re

phone = '+7 955 555-55-55'

if re.findall(r'[^\s\d+\-()]', phone):
    print('Номер не валиден')
else:
    phone = re.sub(r'\D', '', phone)
    if not((len(phone) == 10 and phone[0] == '9') or
           (len(phone) == 11 and phone[0:2] in ['79', '89'])):
        print('Результат: Номер не валиден')
    else:
        phone = phone[-10:]
        print(f'Результат: +7-{phone[0:3]}-{phone[3:6]}-{phone[6:8]}-{phone[8:10]}')

# примеры
# phone = '+7 955 555-55-55'
# phone = '8(955)555-55-55'
# phone = '+7 955 555 55 55'
# phone = '7(955) 555-55-55'
# phone = '423-555-55-5555'
# phone = '123-456-789'
# phone = '79123456789'
# phone = '89123456789'
# phone = '9123456789'
