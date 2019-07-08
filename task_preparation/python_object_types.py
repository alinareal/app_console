# -*- coding: utf-8 -*-
import math
import random
import re


# Числа
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



