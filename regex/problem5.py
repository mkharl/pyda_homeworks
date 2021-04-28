import re

some_text = """Эталонной реализацией Python является интерпретатор CPython, поддерживающий большинство
активно используемых платформ. Он распространяется под свободной лицензией Python Software Foundation License, 
позволяющей использовать его без ограничений в любых приложениях, включая проприетарные"""

vows = len(re.findall(r'(?i)\b([аеёиоуыэюяaeiouy].(\w)+)\b', some_text))
cons = len(re.findall(r'(?i)\b([бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvxz].(\w)+)\b', some_text))

print(f'Слов на гласные буквы: {vows}')
print(f'Слов на согласные буквы: {cons}')
