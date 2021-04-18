# подробной обработки исключительных ситуаций здесь нет

# где-то сделано не совсем, как требуется в задании, например, при перемещении документа
# нет смысла спрашивать у пользователя номер полки, если номер документа уже введен некорректно

# осознанно оставил дублирование кода для выводимых сообщений плюс для более сложных функция
# логика не всегда инкапсулирована в функции - например, часть проверок делается при считывании входных данных
# в функции perform_command; все-таки, думаю, в таком задании это допустимо

documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def print_shelves_list():
    print(f"Текущий перечень полок: {', '.join(sorted(directories))}.")


def is_empty_shelf(shelf):
    return len(directories[shelf]) == 0


def is_doc_id_available(doc_id):
    return doc_id not in [doc['number'] for doc in documents]


def get_doc_by_id(doc_id):
    res = list(filter(lambda doc: doc['number'] == doc_id, documents))
    return res[0] if len(res) != 0 else None


def find_shelf_by_doc_id(doc_id):
    res = list(filter(lambda shelf: doc_id in directories[shelf], directories))
    return res[0] if len(res) != 0 else None


def p(doc_id):
    doc = get_doc_by_id(doc_id)
    if doc is not None:
        print(f"Владелец документа: {doc['name']}")
    else:
        print('Документ не найден в базе')


def s(doc_id):
    shelf = find_shelf_by_doc_id(doc_id)
    if shelf is not None:
        print(f"Документ хранится на полке: {shelf}")
    else:
        print('Документ не найден в базе')


def l():
    print('Текущий список документов:')
    for doc in documents:
        print(f"№: {doc['number']}, тип: {doc['type']}, владелец: {doc['name']}, "
              f"полка хранения: {find_shelf_by_doc_id(doc['number'])}")
    pass


def a_s(new_shelf):
    if new_shelf in directories:
        print('Такая полка уже существует. ', end='')
    else:
        directories[new_shelf] = []
        print('Полка добавлена. ', end='')
    print_shelves_list()


def ds(shelf):
    if shelf not in directories:
        print('Такой полки не существует. ', end='')
    elif not is_empty_shelf(shelf):
        print('На полке есть документы, удалите их перед удалением полки. ', end='')
    else:
        directories.pop(shelf)
        print('Полка удалена. ', end='')
    print_shelves_list()


def ad(doc_id, doc_type, doc_owner, shelf):
    if shelf not in directories:
        print('Такой полки не существует. Добавьте полку командой as.')
    else:
        documents.append({'number': doc_id, 'type': doc_type, 'name': doc_owner})
        directories[shelf].append(doc_id)
        print('Документ добавлен. ', end='')
    l()


def d(doc_id):
    if get_doc_by_id(doc_id) is None:
        print('Документ не найден в базе.')
    else:
        directories[find_shelf_by_doc_id(doc_id)].remove(doc_id)
        # предполагаю, что так работает быстрее, чем через del
        global documents
        documents = [doc for doc in documents if doc['number'] != doc_id]
        print('Документ удален.')
    l()


def m(doc_id, shelf):
    current_shelf = find_shelf_by_doc_id(doc_id)
    if current_shelf == shelf:
        print(f'Документ {doc_id} уже находится на полке {shelf}!')
    else:
        directories[current_shelf].remove(doc_id)
        directories[shelf].append(doc_id)
        print('Документ перемещен.')
    l()


def perform_command(command):
    if command == 'p':
        print('Введите номер документа:')
        p(input())
    elif command == 's':
        print('Введите номер документа:')
        s(input())
    elif command == 'l':
        l()
    elif command == 'as':
        print('Введите номер полки:')
        a_s(input())
    elif command == 'ds':
        print('Введите номер полки:')
        ds(input())
    elif command == 'ad':
        print('Введите номер документа:')
        doc_id = input()
        if not is_doc_id_available(doc_id):
            print(f'Документ с номером {doc_id} уже существует.')
        else:
            print('Введите тип документа:')
            doc_type = input()
            print('Введите владельца документа:')
            doc_owner = input()
            print('Введите полку для хранения:')
            shelf = input()
            ad(doc_id, doc_type, doc_owner, shelf)
    elif command == 'd':
        print('Введите номер документа:')
        d(input())
    elif command == 'm':
        print('Введите номер документа:')
        doc_id = input()
        if get_doc_by_id(doc_id) is None:
            print('Документ не найден в базе.')
            l()
        else:
            print('Введите номер полки:')
            shelf = input()
            if shelf not in directories:
                print('Такой полки не существует. ')
                print_shelves_list()
            else:
                m(doc_id, shelf)
    else:
        print('Неизвестная команда!')


while True:
    print('Введите команду:')
    cmd = input()
    if cmd == 'q':
        break
    else:
        perform_command(cmd.strip())
