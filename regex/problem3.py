import re

# можно ли как-то сделать с помощью re.sub? я не смог найти информацию, как в нем использовать для замены
# 1 символ match-а
x = 'Ultimate fighting Championship'
p = re.compile(r'\b([\w]+)\b')
matches = p.finditer(x)
for match in matches:
    print(match[0][0].upper(), end='')
