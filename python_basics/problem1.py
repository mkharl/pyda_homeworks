phrase_1, phrase_2 = 'str1', 'str2'

if len(phrase_1) == len(phrase_2):
    result = 'Фразы равной длины'
elif len(phrase_1) > len(phrase_2):
    result = 'Фраза 1 длиннее фразы 2'
else:
    result = 'Фраза 2 длиннее фразы 1'

print(result)
