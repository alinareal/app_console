print(dir(dict))
# print(help(dict))

happy_dict = {}

my_dict = {'mother': 'Nina',
           'father': 'Tolya',
           'daughter': 'Alina',
           'son': 'Anton'}

good_dict = {'name': {'first': 'Alina', 'last': 'Laevskaya'}}

his_dict = dict(color='red', type='lips')
print(his_dict)

keyslist = ['1', '2', '3']
valslist = ['a', 'b', 'c']
D = dict(zip(keyslist, valslist))
print(D)

D = dict.fromkeys(['a', 'b'])
print(D)

print(my_dict['mother'])
print(good_dict['name']['last'])

print('father' in my_dict)

print(my_dict.keys())
print(my_dict.values())

print(my_dict.items())

fun_dict = my_dict.copy()
print(fun_dict)

# print(fun_dict.get())

my_dict.update(his_dict)
print(my_dict)

my_dict.pop('type')

print(my_dict)

print(len(my_dict))

my_dict['pet'] = 'Roman'
print(my_dict)

del my_dict['color']
print(my_dict)

print(list(my_dict.keys()))  # version 3.0

D = {x: x*2 for x in range(10)}
print(D)

print(my_dict.get('mother'))
print(my_dict.get('mothers'))
print(my_dict.get('mothers', 0))

print(my_dict.pop('mother'))

table = {'Python': 'Guido van Rossum',
         'Perl': 'Larry Wall',
         'Tcl': 'John Ousterhout'}

for lang in table:
    print(lang, table[lang])

D = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
print(D)

D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(D)

print(my_dict.has_key('father'))

print('father' in my_dict)

n_list = [0] * 5
print(n_list)

D = dict.fromkeys(['a', 'b'], 0)
print(D)
