empty_tuple = ()
print(empty_tuple)

el_tuple = ('hi',)
print(el_tuple)

big_tuple = (1, 4.9, 'me', True,)
print(big_tuple)

huge_tuple = 1, 4.9, 'me', True,
print(huge_tuple)

nested_tuple = (1, (1, (1, (1,))),)
print(nested_tuple)

my_tuple = tuple('alina')
print(my_tuple)

print(my_tuple[2])

print(nested_tuple[1][1][1])

print(my_tuple[1:-1])

print(len(nested_tuple))
print(my_tuple + nested_tuple)

print(my_tuple * 4)

for letter in my_tuple:
    print(letter * 2)

print('a' in my_tuple)
print('v' in my_tuple)

print([i * 2 for i in my_tuple])

print(my_tuple.index('n'))
print(my_tuple.count('a'))

x = (25)
print(x)

print(tuple(sorted(list(my_tuple))))

print([i * 2 for i in my_tuple])

cool_tuple = (1, 2, [3, 4])
cool_tuple[2][1] = 'alina'
print(cool_tuple)
