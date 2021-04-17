import math


print('Введите тип фигуры:')
t = input().lower()

if t == 'круг':
    print('Введите радиус круга:')
    r = int(input())
    s = math.pi * (r ** 2)
elif t == 'прямоугольник':
    print('Введите длину стороны A:')
    a = int(input())
    print('Введите длину стороны B:')
    b = int(input())
    s = a * b
elif t == 'треугольник':
    print('Введите длину стороны A:')
    a = int(input())
    print('Введите длину стороны B:')
    b = int(input())
    print('Введите длину стороны С:')
    c = int(input())
    p = (a + b + c) / 2
    s = pow(p * (p - a) * (p - b) * (p - c), 0.5)
else:
    raise Exception('Неизвестный тип фигуры!')

print(f'Площадь {t}а: {round(s, 2)}')
