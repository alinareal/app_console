# -*- coding: utf-8 -*-
import string

import sys
from string import maketrans

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

family = '{0}, {1} and {2}.'
print(family.format('Nina', 'Tolya', 'Alina'))

family = '{mother}, {father} and {daughter}.'
print(family.format(mother='Nina', daughter='Alina', father='Tolya'))

family = '{1}, {0} and {2}.'
print(family.format('Nina', 'Tolya', 'Alina'))

print('{1}, {0} and {2}.'.format('Nina', 'Tolya', 'Alina'))

form_family = '{1}, {0} and {2}.'.format('Nina', 'Tolya', 'Alina')
print(form_family.replace('Tolya', 'Anatoliy'))

print('My {1[spam]} runs {0.platform}'.format(sys, {'spam': 'laptop'}))
print('My {config[spam]} runs {sys.platform}'.format(sys=sys, config={'spam': 'laptop'}))

print('{0:10} = {1:10}'.format('spam', 123.4567))

print('{0:e}, {1:.3e}, {2:g}'.format(3.14159, 3.14159, 3.14159))
print('{0:f}, {1:.2f}, {2:06.2f}'.format(3.14159, 3.14159, 3.14159))

print('{0:X}, {1:o}, {2:b}'.format(25, 25, 25))

print(format(1.2345, '.2f'))

print('{0:,d}'.format(999999999999))

# String methods
print('my name is archi.'.capitalize())

print('my name is archi.'.center(25))

print('my name is archi.'.count('a'))

print('my name is archi.'.endswith('i'))
print('my name is archi.'.endswith('.'))

print('my name is archi.'.find('y'))
print('my name is archi.'.find('f'))

print('my name is archi.'.index('s'))

print('gdx4w3gd4444'.isalnum())

print('my name is archi'.isalpha())

# print('45333333'.isdecimal())

print('333334'.isdigit())

# print('Python'.identifier())

print('ASSSGfhFD'.islower())
print('trete'.islower())

# print('534444'.isnumeric())
# print('What is your name?'.isprintable())

print('     '.isspace())
print('fdgdg'.isspace())

print('The Weather'.istitle())
print('The weather'.istitle())

print('The weather'.isupper())
print('THE WEATHER'.isupper())

print('-'.join('WEATHER'))

print('Dimash'.ljust(10, '#'))
print('Dimash'.rjust(10, '#'))

print('NONNA'.lower())

print('     I want to eat'.lstrip())
print('https://www.google.com/'.lstrip('htps:/.'))

print('I want to eat            '.rstrip())
print('https://www.google.com/'.rstrip('.com/'))

print('I want to eat'.replace('eat', 'sleep'))

print('I want to sleep'.rfind('e'))
print('I want to sleep'.rfind('f'))


print('I want to sleep'.rindex('e'))
# print('I want to sleep'.rindex('j'))

print('I want to sleep'.split())

txt = 'Thank you for the music\nWelcome to the jungle'
x = txt.splitlines()
print(x)

print('I want to sleep'.startswith('I'))
print('I want to sleep'.startswith('f'))

print('     I want to sleep      '.strip())

print('I want TO sleep'.swapcase())

print('I want TO sleep'.title())

print('I want TO sleep'.upper())

txt = '50'
x = txt.zfill(10)
print(x)

print('I want to sleep'.partition('to'))
print('I want to sleep and to play'.rpartition('to'))

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!"
print str.translate(trantab)
