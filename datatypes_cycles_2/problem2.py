queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

res = {}
total = 0
for q in queries:
    cnt = len(q.split())
    res.setdefault(cnt, 0)
    res[cnt] += 1
    total += 1

for k, v in sorted(res.items()):
    print(f'Поисковых запросов, содержащих {k} слов(а): {round(100 * v / total, 2)}%')
