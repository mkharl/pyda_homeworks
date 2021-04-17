width = 10
length = 205
height = 5

# все условия ниже взаимоисключающие
if width < 15 and length < 15 and height < 15:
    result = 'Коробка №1'
elif (15 < width < 50) or (15 < length < 50) or (15 < height < 50):
    result = 'Коробка №2'
elif length > 200:
    result = 'Упаковка для лыж'
else:
    result = 'Стандартная коробка №3'

print(result)
