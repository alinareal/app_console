my_str = 'Alina'
while my_str:
    print(my_str)
    my_str = my_str[1:]

# a = 0; b = 10
# while a < b:
#     print(a)
#     a += 1

a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)

b = 0
while b < 10:
    b += 1
    if b % 2 != 0:
        print(b)

# while True:
#     name = raw_input('Enter name: ')
#     if name == 'stop':
#         break
#     age = raw_input('Entter age: ')
#     print('Hello ' + name + '!')

my_list = [2, 5, 6.7]
for i in my_list:
    print(i)

my_sum = 0
for i in my_list:
    my_sum += i

prod = 1
for i in my_list:
    prod *= i

print(my_sum)
print(prod)

for i in 'asdf':
    print(i)

for i in ('and', 'I"m', 'okay'):
    print(i)

T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:
    print(a, b)

my_dict = {'me': 'Alina', 'mother': 'Nina', 'father': 'Tolya'}

for key in my_dict:
    print(key + ' is ' + my_dict[key])

for (key, value) in my_dict.items():
    print(value + ' is ' + key)

for both in my_dict.items():
    family, name = both
    print(family)
    print(name)

for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:
    print(a, b, c)

for ((a, b), c) in [([1, 2], 3), ['XY', 6]]:
    print(a, b, c)

items = ['aaa', 111, (4, 5), 2.01]
tests = [(4, 5), 3.14]

for key in tests:
    for item in items:
        if item == key:
            print(key, 'was found')
            break
    else:
        print(key, 'not found!')

for key in tests:
    if key in items:
        print(key, 'was found')
    else:
        print(key, 'not found!')

seq1 = 'alina'
seq2 = 'alinona'
res = []

for i in seq1:
    if i in seq2:
        res.append(i)

print(res)

my_file = open('alina.txt')
# print(my_file.read())

# for char in my_file.read():
#     print(char)

# for line in my_file.readlines():
#     print(line)

for line in my_file:
    print(line)

print(range(10))
print(range(3, 9))
print(range(4, 16, 3))
print(range(6, -4, -1))

for i in range(4):
    print(i * 2)

for i in 'alina':
    print(i)

my_str = 'alinochka'
for i in range(0, len(my_str), 2):
    print(my_str[i])

for i in my_str[::2]:
    print(i)

my_list = [3, 4, 5, 6]
for i in range(len(my_list)):
    my_list[i] +=1

print(my_list)

L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
print(zip(L1, L2))

for (x, y) in zip(L1, L2):
    print('{} + {} = {}'.format(x, y, x+y))

T1, T2, T3 = (1, 2, 3), (4, 5, 6), (7, 8, 9)
print(zip(T1, T2, T3))

print(zip('asd', 'fghjkl'))
print(map(None, 'asd', 'fghjkl'))

print(map(ord, 'asdfg'))

keys = ['name', 'age', 'is_volunteer']
vals = ['Alina', 19, True]
D = {}

for (key, val) in zip(keys, vals):
    D[key] = val

print(D)

D1 = dict(zip(keys, vals))
print(D1)

print(list(enumerate('alina')))
for (pos, item) in enumerate('alina'):
    print('{} is on position {}'.format(item, pos))

s = enumerate('alina')
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
