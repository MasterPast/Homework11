import re
from datetime import date, datetime, timedelta
qqq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
www = {'1': 'om', '2':'ee', '3':'dss', '4':'qww', '5':'xccv', '6':'cvcxv', '7':'thr', '8':'thrdfdf', '9':'jhjk', '10':'ten'}


class Field():
    def __init__(self, value):
        self.value = value
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value == 2 or new_value == 4:
            self.__value = new_value

class Cust_iter:
    def __iter__(self):
        return Iterable()


class Iterable:
    MAX_VALUE = 3

    def __init__(self):
        self.current_value = 0

    def __next__(self):
        if self.current_value < self.MAX_VALUE:
            self.current_value += 1
            return self.current_value
        raise StopIteration


class Qqq(Field):
    ...

# print(qqq[2])

x = 0
# r = Field(2)
# e = Field(4)

# r.value = 2
# # print(r.value)
# st = 'qwertyu'

# st1 = st[:3]
# print(st1)

c=Cust_iter()

# print(f'>>>{len(www)}')

while x < len(qqq):
    m = input()
    for _ in c:
        print(_+  x)
    print(f'in>>> {x}')
    x += _



# # '^(?:[( )-]*\d){10}[()-]*$' # UA-10
# new_value = '9999-88-89'
# # new_value = '9998888999'
# sovp = re.findall('^(\d){4}-(\d){2}-(\d){2}$', new_value)
# # sovp = re.findall('^(\d){10}$', new_value)
# print(sovp)
# if sovp != []:
#     #     while not sovp[0].isdigit():
#     #         check_dig = sovp[0]
#     #         for char in check_dig:
#     #             if not char.isdigit():
#     #                 sovp[0] = sovp[0].replace(char, '')
#     # self.__value = new_value
#     print(new_value)
# else:
#     print('No')

# print(type(eval))

# today = datetime.today().date()
# print(today)
# bir = '1982-11-04'
# birth = datetime.strptime(bir, '%Y-%m-%d')
# print(birth.date())
# today_date = datetime(year=1, month=today.month, day=today.day)
# birth_date = datetime(year=1, month=birth.month, day=birth.day)
# delta_day = today_date - today_date
# a = birth_date - today_date
# print(today_date > birth_date)
# if today_date < birth_date:
#     print(a)
# elif today_date > birth_date:
#     today_date = datetime(year=1, month=today.month, day=today.day)
#     birth_date = datetime(year=2, month=birth.month, day=birth.day)
#     a = birth_date - today_date
#     print(a)
# else:
#     print('TODAY is Birthday!!!')
