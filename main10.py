from collections import UserDict
import re


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

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
print(book)
book.delete("Jane")
print(book)