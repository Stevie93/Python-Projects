from datetime import datetime, timedelta
from array import array

# first_name = input('Enter first name: ')
# last_name = input('Enter last name: ')
# name = f'{first_name} {last_name}'
# out = 'Hello '
# out += name
# print(out)

# print(datetime.now().month)


# try:
#     print(x/y)
# except ZeroDivisionError as e:
#     print('Not allowed')
# else:
#     pass
# finally:
#     print('done')

# names = ['test1', 'test2']
# names.append(str(8))
# names.sort()
# shortList = names[:2]
# # print(len(names))
# # print(names)
# # print(shortList)

# # for name in names:
# #     names.append('rogue')
# #     print(name)

# index = len(names)-1

# while index >= 0:
#     print(names[index])
#     index -= 1
# from helpers import display


# def sum(a, b):
#     return a + b


# c = sum(4, 5)

# display(c)


class Presenter:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        print("in the getter")
        return self.__name

    @name.setter
    def name(self, value):
        print("in the setter")
        self.__name = value


presenter = Presenter('Chris')
presenter.name = 'Christopher'
print(presenter.name)
