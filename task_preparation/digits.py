# -*- coding: utf-8 -*-
import math
import random
import decimal
from decimal import Decimal
from fractions import Fraction


# Группировка подвыражений с помощью круглых скобок
print(2 + 3 * 4)
print(2 + (3 * 4))
print((2 + 3) * 4)


# Смешивание типов и их преобразование
print(3 + 2.4)
print(3 + 2)
print(3 + 2.0)
print(3 + 2 + 4j)
print(3.0 + 2 + 4j)

print(int(2.4))
print(float(2))

print(int('4') + 5)
print('4' + str(5))


# Переменные и простые выражения
dogs = 7
cats = 4
print(dogs + 3)
print(dogs + 3, dogs + 2)
print(dogs % 2, dogs ** 2)
print(dogs % 2, dogs ** 2.0)
print(dogs / (2.0 + cats))
print(dogs / 2 + cats)
print(dogs / 2.0 + cats)


# Форматы отображения чисел
num = 1 / 3.0
print(type(num))
print(num)

print('%e' % num)
print('%4.2f' % num)

num = '{0:4.2f}'.format(num)
print(num)
print(type(num))


# Операции сравнения: простые и составные
print(4 < 2.0)
print(4 >= 2)
print(4.0 >= 2)
print(4 == 2.0)
print(4.0 != 2.0)

a = 12
b = 14
c = 16

print('---------')
print(a < b < c)
print(a < b and b < c)
print(a < b > c)
print(a < b and b > c)

print(1 < 2 < 3 < 4 < 5 < 6 < 7 < 8 < 9 < 10)
print(1 == 2 < 3)
print(False < 3)


# Деление: классическое, с округлением вниз и истинное
print(10 / 4)
print(10 / float(4))
print(10 // 4)
print(10 / 4.0)
print(10 // 4.0)


# Округление вниз и усечение дробной части
print(math.floor(4.7))
print(math.floor(-4.7))
print(math.trunc(4.7))
print(math.trunc(-4.7))

print(5 / 2, 5 / -2)
print(5 // 2, 5 // -2)
print(5 / 2.0, 5 / -2.0)
print(5 // 2.0, 5 // -2.0)


# Точность представления целых чисел
huge_number = 999999999999999999999999999999999999999999 + 1
print(huge_number)
print(type(huge_number))
print(2 ** 200)

# Комплексные числа
print(1j * 1J)
print(2 + 1j * 3)
print((2 + 1j) * 3)
print((3 + 2j) * (4 - 3j))


# Шестнадцатеричная, восьмеричная и двоичная формы записи чисел
print(0x01, 0x10, 0xFF)  # Шестнадцатеричные литералы
print(0o1, 0o20, 0o377)  # Восьмеричные литералы
print(0b1, 0b10000, 0b11111111)  # Двоичные литералы

print(hex(19))
print(oct(19))
print(bin(19))

print(int('19'))
print(int('64'), int('100', 8), int('40', 16), int('1000000', 2))
print(int('0x40', 16), int('0b1000000', 2))
print(eval('64'), eval('0o100'), eval('0x40'), eval('0b1000000'))
print('{0:o}, {1:x}, {2:b}'.format(64, 64, 64))
print('%o, %x, %X' % (64, 255, 255))

print(0o1, 0o20, 0o377)
print(01, 020, 0377)


# Битовые операции
num1 = 1
print(num1 << 2)
print(num1 | 2)
print(num1 & 1)

num2 = 0b010101
print(num2 << 3)
print(bin(num2 << 3))
print(bin(num2 | 0b001))
print(bin(num2 & 0b001))

num3 = 0x403F
print(bin(num3))
print(num3 ^ 0b01)
print(bin(num3 ^ 0b01))

print(int('1010101', 2))
print(hex(85))

num4 = 99
print(bin(num4), num4.bit_length())
print(len(bin(99)) - 2)


# Другие встроенные средства для работы с числами
print(math.pi, math.e)
print(math.sin(2 * math.pi / 180))
print(math.sqrt(196))
print(pow(2, 6))
print(abs(-123), abs(123))
print(sum((-2, -1, 3, 4)))
print(min(1, 2, 3, 4, 5, 6))
print(max(1, 2, 3, 4, 5, 6))

print(math.floor(4.632), math.floor(-4.632))
print(math.trunc(4.632), math.trunc(-4.632))
print(int(4.632), int(-4.632))
print(round(4.632), round(4.332), round(4.638, 2))
print('%.1f' % 2.567, '{0:.2f}'.format(2.567))

print(math.sqrt(16))
print(pow(16, .5))
print(16 ** .5)

print(random.random())
print(random.random())
print(random.random())

print(random.randint(50, 100))
print(random.randint(50, 100))
print(random.randint(50, 100))

print(random.choice(['Alina', 'Dima', 'Ksusha']))
print(random.choice(['Alina', 'Dima', 'Ksusha']))
print(random.choice(['Alina', 'Dima', 'Ksusha']))


# Числа с фиксированной точностью
print(0.1 + 0.1 + 0.1 - 0.3)
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
print(Decimal('0.1') + Decimal('0.10') + Decimal('0.1') - Decimal('0.30'))


# Глобальная настройка точности
print(decimal.Decimal(1) / decimal.Decimal(7))

decimal.getcontext().prec = 4
print(decimal.Decimal(1) / decimal.Decimal(7))

print(1999 + 1.33)
decimal.getcontext().prec = 2
print(decimal.Decimal(str(1999 + 1.33)))


# Менеджер контекста объектов класса Decimal
with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))


# Рациональные числа
a = Fraction(3, 5)
b = Fraction(2, 4)

print(a)
print(b)

print(a + b)
print(a - b)
print(a * b)
print(a / b)

c = Fraction('.75')
print(c)


# Точность
print(0.1 + 0.1 + 0.1 - 0.3)
print(Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10))


# Преобразование и смешивание в выражениях значений разных типов
print((2.5).as_integer_ratio())

f = 2.5
z = Fraction(*f.as_integer_ratio())
print(z)

print(float(z))

print(Fraction.from_float(4.5))
print(Fraction(*(4.5).as_integer_ratio()))

magic_number = Fraction(3, 5)
print(magic_number + 2)
print(magic_number + 2.0)
print(magic_number + Fraction(2, 7))


# Множества
m = set('gdfshdg')
n = set('sdgjfjscvbn')
print(m)
print(n)
print('s' in m)
print(m - n)
print(m | n)
print(m & n)
print(m ^ n)
print(m > n, m < n)

print(dir(set))

z = m.intersection(n)
print(z)
z.add('Alla')
print(z)
z.update(set(['Ira', 'Olga']))
print(z)
z.remove('s')
print(z)

for item in m:
    print(item * 3)

print(type(m))
print(type({}))


# Генераторы множеств
v = {x ** 2 for x in [1, 2, 3, 4]}
print(v)

print({x for x in 'dima'})
print({x * 3 for x in 'dima'})

# Удаление повторяющихся значений
magic_list = [2, 5, 4, 2, 6, 4, 8, 8]
result = list(set(magic_list))
print result


# Логические значения
print(type(True))
print(type(False))
print(isinstance(True, int))
print(isinstance(False, int))
print(True == 1)
print(False == 0)
print(True is 1)
print(False is 0)
print(True or False)
print(True and False)
print(True + 44)


# Контрольные вопросы

# 1
print(2 * (3 + 4))  # 14

# 2
print(2 * 3 + 4)  # 10

# 3
print(2 + 3 * 4)  # 14

# 4
print(math.sqrt(34))
print(pow(34, .5))
print(34 ** .5)

print(3 ** 2)
print(pow(3, 2))

# 5
print(type(1 + 2.0 + 3))  # float

# 6
good_number = 5.854
print(math.trunc(good_number))
print(int(good_number))
print(round(good_number))
print(math.floor(good_number))

# 7
print(float(7))

# 8
our_number = 45
print(hex(our_number))
print(oct(our_number))
print(bin(our_number))

# 9
print(int('0x2d', 16))
print(int('055', 8))
print(int('0b101101', 2))
