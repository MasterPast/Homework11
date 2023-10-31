import re
from sys import exit
from collections import deque
from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    ...


class Phone(Field):
    def __init__(self, value):  # регуляр телефона 10
      
        # '^(?:[( )-]*\d){10}[()-]*$' # UA-10
        sovp = re.findall('^(\d){10}$', value)
        if sovp != []:
            while not sovp[0].isdigit():
                check_dig = sovp[0]
                for char in check_dig:
                    if not char.isdigit():
                        sovp[0] = sovp[0].replace(char, '')
            self.value = value
        else:
            raise ValueError

    def __str__(self):
        return self.value


class Birthday(Field):
    def __init__(self, value):
        ...


class Record:
    def __init__(self, name):
    
        self.name = Name(name)
        self.phones = []
        self.birthday = ''

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, old, new):
    
        edit_phone_result = False
        for ph in self.phones:
            if str(ph) == str(new):
                edit_phone_result = True
        for ph in self.phones:
            if str(ph) == str(old) and edit_phone_result == False:
                edit_phone_result = True
                self.phones.pop(self.phones.index(ph))
                self.phones.append(Phone(new))
        if edit_phone_result == False:
            raise ValueError

    def find_phone(self, phone):

        find_phone_result = False
        for ph in self.phones:
            if str(ph) == str(phone):
                find_phone_result = True
                return ph
        if find_phone_result == False:
            return None

    def remove_phone(self, phone):

        for ph in self.phones:
            if str(ph) == str(phone):
                self.phones.pop(self.phones.index(ph))

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    
    def add_record(self, record):
        self[record.name.value] = record 

    def find(self, name):

        for nam, record in self.data.items():
            if nam == name:
                return record
            
    def delete(self, name):

        if name in self.data:
            print('Yep')
            self.data.pop(name)



def input_error(fn):
    def inner(cmnd):

        try:
            msg = fn(cmnd)
        # except KeyError:
        #     msg = '\nSomething not good...((( Please, check HELP with "help" command.'
        except IndexError:
            msg = '\nWaiting for contact`s name and number phone.'
        except UnboundLocalError:
            msg = '\nCan`t find this contact in your pnonebook. Use "show all" to check.'
        # except ValueError:
        #     msg = '\nSomething not good...((( Please, check HELP with "help" command.'

        return msg
    return inner


@input_error
def add(cmnd):

    voc_contacts = {}
    voc_contacts['name'] = cmnd[0]
    voc_contacts['phone'] = cmnd[1]
    list_voc_contacts.append(voc_contacts)
    msg = f'\nIt was added: {voc_contacts["name"]} with phone number: {voc_contacts["phone"]} in your contacts.'

    return msg


@input_error
def change(cmnd):
    for voc in filter(lambda voc: voc['name'] == cmnd[0], list_voc_contacts):

        voc.update([('phone', cmnd[1])])
        msg = f'\nIt was changed the phone number of: {voc["name"]} on: {voc["phone"]}.'

    return msg


def exit_bot(cmnd):

    msg = '\nGood bye! Have a nice day!'
    return msg


def help(cmnd):

    msg = '\nHelp for you:\n\n'
    for d1 in voc_help.items():
        msg += d1[1]

    return msg


def hello(cmnd):

    msg = '\nHello! How can I help you?'
    return msg


@input_error
def phone(cmnd):

    for voc in filter(lambda voc: voc['name'] == cmnd[0], list_voc_contacts):
        msg = f'\nFor contact: {voc.get("name")} I found this phone number: {voc["phone"]}.'

    return msg


@input_error
def show_all(cmnd):

    msg = '\nI found next information in your contacts:\n'
    msg += (('-' * 46) + '\n')
    for contacts in list_voc_contacts:
        cont_string = '| {a1:{align}{width}} | {a2:{width}}|\n'.format(
            a1=contacts['name'], a2=contacts['phone'], align='>', width=20)
        msg += cont_string
    msg += (('-' * 46) + '\n')

    return msg


def talking(cmnd):

    for pair in voc_cmnd:

        patt = re.compile('(?i)' + pair + ' ')
        s = patt.match(cmnd + ' ')
        if s != None:
            cmnd = cmnd.split()
            cmnd = deque(cmnd)
            if cmnd[0] == 'good' or cmnd[0] == 'show':
                cmnd[0] += ' ' + cmnd[1]
                voc_func = cmnd.popleft().lower()
                cmnd.popleft()
            else:
                voc_func = cmnd.popleft().lower()
            break
    if s == None:
        voc_func = 'unknown'

    return voc_cmnd[voc_func], cmnd


def unknown(cmnd):

    msg = '\nPlease, repeat... Don`t understand you.((( You can use HELP command.'
    return msg


input_command = ''
list_voc_contacts = []
voc_cmnd = {
    'add': add,
    'change': change,
    'close': exit_bot,
    'exit': exit_bot,
    'good bye': exit_bot,
    'hello': hello,
    'help': help,
    'phone': phone,
    'show all': show_all,
    'unknown': unknown
}

voc_help = {'add': 'add contact phone : Add contact and phone number in phonebook.\n',
            'change': 'change contact phone : Change contact`s phone number on new in phonebook.\n',
            'close': 'close : Close the bot.\n',
            'exit': 'exit : Close the bot.\n',
            'good bye': 'good bye : Close the bot.\n',
            'hello': 'hello : Greeting you))).\n',
            'help': 'help : Display this screen with commands and parameters.\n',
            'phone': 'phone contact: Display the contact`s phone.\n',
            'show all': 'show all : Display your phonebook.'
            }


def main():
    
    # # Створення нової адресної книги
    # book = AddressBook()

    # # Створення запису для John
    # john_record = Record("John")
    # john_record.add_phone("1234567890")
    # john_record.add_phone("5555555555")

    # # Додавання запису John до адресної книги
    # book.add_record(john_record)

    # # Створення та додавання нового запису для Jane
    # jane_record = Record("Jane")
    # jane_record.add_phone("9876543210")
    # book.add_record(jane_record)

    # # Виведення всіх записів у книзі
    # for name, record in book.data.items():
    #     print(record)

    # # Знаходження та редагування телефону для John
    # john = book.find("John")
    # john.edit_phone("1234567890", "1112223333")

    # print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # # Пошук конкретного телефону у записі John
    # found_phone = john.find_phone("5555555555")
    # print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # # Видалення запису Jane
    # book.delete("Jane")
    while True:
        input_command = input('\nWhat can I do for you? >>> ')
        res, cmnd = talking(input_command)
        msg = res(cmnd)
        print(msg)
        if msg == '\nGood bye! Have a nice day!':
            exit()


if __name__ == '__main__':
    main()

