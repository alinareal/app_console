# -*- coding: utf-8 -*-
import math
import random
import re


# Числа
from decimal import Decimal

print(math.e)
print(math.sqrt(6465))
print(random.random())
print(random.choice([11, 24, 32, 48]))


# Строки
my_string = 'Alinona'

print(len(my_string))

print(my_string[2])
print(my_string[-2])
print(my_string[len(my_string) - 2])

print(my_string[3:6])
print(my_string[2:])
print(my_string[:4])
print(my_string[:-1])
print(my_string[:])

print(my_string + 'ya')
print(my_string * 3)

print(my_string.find('ona'))
print(my_string.find('ofk'))

print(my_string.replace('on', 'ab'))
print(my_string)

super_line = 'me!myself!I       '
print(super_line)
print(super_line.split('!'))
print(super_line.upper())
print(super_line.isalpha())
print(super_line.rstrip())

print('%s plays football with %s.' % ('Antony', 'Matvey'))
print('{1} plays football with {0}.'.format('Antony', 'Matvey'))

print(dir(super_line))
print(help(super_line.endswith))

S = 'A\nB\tC'
print(len(S))

match = re.match('Hello[ \t]*(.*)world', 'Hello Python world')
print(match.group(1))

match = re.match('/(.*)/(.*)/(.*)', '/usr/home/lumberjack')
print(match.groups())


# Списки
super_list = ['Flower', 'Bird', 'Tree']

print(len(super_list))
print(super_list[1])

print(super_list[:-1])
print(super_list + ['me', 'myself', 'I'])
print(super_list)

happy_list = ['Rompasso', 22.2, True, 'Filatov & Karas']
happy_list.append(123.4)
print(happy_list)

happy_list.pop(2)
print(happy_list)

del happy_list[1]
print(happy_list)

happy_list.insert(0, 'L.B.One')
print(happy_list)

happy_list.remove(123.4)
print(happy_list)

happy_list.sort()
print(happy_list)

happy_list.reverse()
print(happy_list)

# print(happy_list[12])

matrix_list = [[1, 2, 3],
               [6, 7, 9],
               [5, 4, 7]]

print(matrix_list)
print(matrix_list[2])
print(matrix_list[2][1])

col1 = [row[0] for row in matrix_list]
print(col1)

col = [row[1] / 2 for row in matrix_list if row[1] % 2 == 0]
print(col)

diag = [matrix_list[i][i] for i in [0, 1, 2]]
print(diag)

doubles = [letter * 3 for letter in 'alina']
print(doubles)

# Словари
my_dict_1 = {'name': 'Alina', 'status': 'Volunteer', 'place': 'Falcon Club'}

print(my_dict_1['status'])

my_dict_2 = {}
my_dict_2['surname'] = 'Robinson'
my_dict_2['age'] = 28
my_dict_2['married'] = True

print(my_dict_2)

information = {'nickname': 'Rompasso',
               'name': {'first': 'Roman', 'last': 'Krylov'},
               'job': ['dj', 'sound_maker'],
               'age': 23}

print(information['nickname'])
print(information['name'])
print(information['job'])
print(information['age'])

print(information['name']['first'])
print(information['name']['last'])

print(information['job'][0])
print(information['job'][-1])


information['job'].append('electronic_music_maker')
print(information)

print(information.keys())
print(information.values())

D = {'a': 1, 'c': 2, 'b': 3}
for i in sorted(D):
    print(i, ': ', D[i])

x = 4
while x > 0:
    print('spam!' * x)
    x -= 1

squares = [i ** 2 for i in [2, 5, 3, 6, 4]]
print(squares)

squares = []
for i in [2, 5, 3, 6, 4]:
    squares.append((i ** 2))

print(squares)

print('a' in D)
print('n' in D)

if not 'f' in D:
    print('missing')

if 'n' not in D:
    print('missing')

value = D.get('x', 0)
print(value)

value = D['z'] if 'z' in D else 2
print(value)

# Кортежи
magic_tuple = ('a', 'b', 'c', 'd')
print(len)


d = Decimal(2000)

print d





















