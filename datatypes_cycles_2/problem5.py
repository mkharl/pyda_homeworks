my_list = [1, 2, 3, 4, 5]

if len(my_list) == 0:
    res = {}
elif len(my_list) == 1:
    raise Exception('Нельзя сформировать словарь из одного элемента!')
else:
    res = {my_list[-2]: my_list[-1]}

    for el in reversed(my_list[:-2]):
        res = {el: res.copy()}
