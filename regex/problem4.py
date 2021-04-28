import re

emails = ['test@gmail.com', 'test2@gmail.com', 'xyz@test.in', 'test@ya.ru', 'xyz@mail.ru', 'xyz@ya.ru', 'xyz@gmail.com']
domains = {}

for email in emails:
    domain = re.findall(r'@(.+\..+)', email)[0]
    domains.setdefault(domain, 0)
    domains[domain] += 1

# сначала сортируем по количеству, затем по названию домена
for domain, count in sorted(domains.items(), key=lambda x: (-x[1], x[0])):
    print(f'{domain}: {count}')
