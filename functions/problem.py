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


def p(doc_id):
    res = list(filter(lambda doc: doc['number'] == doc_id, documents))
    if len(res) == 0:
        print('Документ не найден в базе')
    else:
        print(f"Владелец документа: {res[0]['name']}")


def perform_command(command):
    if command == 'p':
        print('Введите номер документа:')
        p(input())
    elif command == 's':
        pass


while True:
    print('Введите команду:')
    cmd = input()
    if cmd == 'q':
        break
    else:
        perform_command(cmd)
