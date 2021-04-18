stats = {
    'facebook': 55,
    'yandex': 115,
    'vk': 120,
    'google': 99,
    'email': 42,
    'ok': 98
}

print(f'Максимальный объем продаж на рекламном канале: {max(stats, key=stats.get)}')
