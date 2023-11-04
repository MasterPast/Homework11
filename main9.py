import re
from sys import exit
from collections import deque


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
    while True:
        input_command = input('\nWhat can I do for you? >>> ')
        res, cmnd = talking(input_command)
        msg = res(cmnd)
        print(msg)
        if msg == '\nGood bye! Have a nice day!':
            exit()


if __name__ == '__main__':
    main()