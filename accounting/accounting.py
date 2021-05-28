from pprint import pprint

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
 #
directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }


# Инициализация доп. функций
def input_doc_number():
    return input('Введите номер документа: ')

def check_doc(doc_number):
    for key, value in directories.items():
        if doc_number in value:
            return True
    return False


def check_doc_index(doc_number):
    for i in range(len(documents)):
        if documents[i]['number'] == doc_number:
            return i
        else:
            return False

def get_shelf(doc_number):
    if check_doc(doc_number) is True:
        for key, value in directories.items():
            if doc_number in value:
                return key

def get_new_shelf():
    return input('Введите номер новой полки: ')

def check_shelf(new_shelf):
    if new_shelf in directories.keys():
        return True
    else:
        return False

def update_doc_in_shelf(doc_number, new_shelf):
    value = directories[new_shelf]
    value.append(doc_number)
    directories[new_shelf] = value
    return doc_number, new_shelf, True

def create_shelf(new_shelf):
    directories[new_shelf]=[]

# Основные методы для исполнения команд
def get_name():
    doc_number=input_doc_number()
    if check_doc(doc_number) is True:
        return documents[check_doc_index(doc_number)]['name']
    else:
        quit()

def get_doc_shelf():
    doc_number=input_doc_number()
    check_doc(doc_number)
    if check_doc(doc_number) is True:
        return get_shelf(doc_number)
    else:
        quit()

def get_doc_list():
    docs = []
    for doc in documents:
        docs.append(set(doc.values()))
    return docs

def add_new_doc():
    new_dic = {}
    doc_number=input('Введите номер документа: ')
    doc_type = input('Введите тип документа: ')
    new_dic['type'] = doc_type
    new_dic['number'] = doc_number
    doc_name = input('Введите имя владельца: ')
    new_dic['name'] = doc_name
    shelf_number = str(input('Введите номер полки, куда положить: '))

    documents.append(new_dic)

    shelf_status = check_shelf(shelf_number)
    if shelf_status is True:
        update_doc_in_shelf(doc_number, shelf_number)
    else:
        create_shelf(shelf_number)
        update_doc_in_shelf(doc_number, shelf_number)
    return new_dic, (shelf_number, directories.get(shelf_number))

def delete_doc():
    doc_number=input_doc_number()
    if check_doc(doc_number) is False:
        quit()
    doc_ind = check_doc_index(doc_number)
    doc_shelf = get_shelf(doc_number)

    documents.pop(doc_ind)
    directories[doc_shelf].remove(doc_number)
    return doc_number, True

def change_doc_shelf():
    doc_number=input_doc_number()
    if check_doc(doc_number) is False:
        quit()
    new_shelf = get_new_shelf()
    doc_shelf = get_shelf(doc_number)
    directories[doc_shelf].remove(doc_number)
    shelf_status = check_shelf(new_shelf)
    if shelf_status is True:
        update_doc_in_shelf(doc_number, new_shelf)
    else:
        create_shelf(new_shelf)
        update_doc_in_shelf(doc_number, new_shelf)

    print(f'Документ перемещен с полки {doc_shelf} на полку {new_shelf}')
    return (new_shelf, directories.get(new_shelf))

def add_new_shelf():
    new_shelf = get_new_shelf()
    shelf_status = check_shelf(new_shelf)
    if shelf_status is True:
        print('Такая полка уже существует')
        return False
    else:
        create_shelf(new_shelf)
        print('Новая полка успешно создана')
        return 'Новая полка успешно создана'

def main():
    command_key = input('Введите команду: ')

    if command_key == 'p':
        print(f'Этот документ принадлежит {get_name()}')
    elif command_key == 's':
        print(f'Документ лежит на полке {get_doc_shelf()}')
    elif command_key == 'l':
        docs = get_doc_list()
        for doc in docs:
            pprint(doc)
    elif command_key == 'a':
        add_new_doc()
        print('Документ успешно добавлен')
        pprint(documents)
        pprint(directories)
    elif command_key == 'd':
        delete_doc()
        print('Документ успешно удален')
        pprint(documents)
        pprint(directories)
    elif command_key == 'm':
        change_doc_shelf()
        pprint(documents)
        pprint(directories)
    elif command_key == 'as':
        add_new_shelf()
        pprint(directories)
    else:
        print('Вы ввели не существующую команду! Введите правильное значение.')

if __name__ == '__main__':
    main()
