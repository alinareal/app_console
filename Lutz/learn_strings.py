# -*- coding: utf-8 -*-
import string

my_str_1 = 'Roger'
my_str_2 = "Federer"

my_str_3 = "It's"
my_str_4 = 'I"ve got'

print(my_str_1)
print(my_str_2)
print(my_str_3)
print(my_str_4)

my_str_5 = 'It"s ' 'my' ' life'  # Неявная конкатенация
print(my_str_5)

my_str_6 = 'It"s ', 'my', ' life'
print(my_str_6)

my_str_7 = 'Love\'s'
print(my_str_7)

my_str_7 = "Love\"s"
print(my_str_7)

my_str_8 = 'me\nmyself\tI'
print(my_str_8)

print(len(my_str_8))

my_str_9 = 's\tp\na\x00m'
print(my_str_9)
print(len(my_str_9))

my_str_10 = 'C:\py\code'
print(my_str_10)
print(len(my_str_10))

my_str_11 = 'C:\my\node'
print(my_str_11)
print(len(my_str_11))

my_str_12 = 'C:\my\\node'
print(my_str_12)
print(len(my_str_12))

# my_file_1 = open('C:\new\text.dat', 'w')
# my_file_2 = open(r'C:\new\text.dat', 'w')
# my_file_3 = open('C:\\new\\text.dat', 'w')

my_path = r'C:\new\text.dat'
print(my_path)

"""
mantra = '''Always look
on the bright
side of life.'''

print(mantra)
"""

bird = 'crouch'
place = 'forest'

print(bird + place)
print(bird * 3)

print('$' * 20)

# print('4' + 9)

my_job = 'hacker'
print('k' in my_job)
print('v' in my_job)

my_str_13 = 'AirDotsLand'
print(my_str_13[3])
print(my_str_13[-1])
print(my_str_13[3:5])
print(my_str_13[::2])
print(my_str_13[::-1])
print(my_str_13[5:2:-1])
print(my_str_13[slice(1, 4)])

print(str(324), int('234'), float('543'))

print('4' + str(9))
print(int('4') + 9)

print(ord('s'))
print(chr(115))

my_str_13 = my_str_13.replace('Air', 'Land')
print(my_str_13)

print('%s plays football with %s.' % ('Antony', 'Matvey'))
print('{1} plays football with {0}.'.format('Antony', 'Matvey'))

print(my_str_13.replace('La', 'No', 2))

print(my_str_13.find('Do'))
print(my_str_13.find('Da'))

my_str_14 = 'Dimash'
my_lst_1 = list(my_str_14)
print(my_lst_1)

my_lst_1[2] = 'v'
print(my_lst_1)

my_str_14 = ''.join(my_lst_1)
print(my_str_14)

print('SPAM'.join(['eggs', 'sausage', 'ham', 'toast']))

my_str_15 = 'dffd. swfeds. rfg. sfd. sdgg'
print(my_str_15.split('.'))
print(my_str_15.split())

my_str_16 = 'What a wonderful weather today         '
print(my_str_1.isalpha())
print(my_str_16.rstrip())
print(my_str_16.upper())
print(my_str_16.endswith('today'))
print(my_str_16.startswith('What'))
print('a' in my_str_16)

S = 'a+b+c+'
y = string.replace(S, '+', 'spam')
print(y)

print('My name is %s.' % 'Alina')
print('My name is %s. I am %d.' % ('Alina', 19))
print('My name is %s. I am %s.' % ('Alina', 19))

print('%(n)d %(x)s' % {'n': 1, 'x': 'spam'})























