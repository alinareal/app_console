# links and copies

main_list = ['d', 5, 'g']
# my_list = [main_list, 3, 78]
my_list = list(main_list)
# my_dict = {'1': main_list, '2': 'f'}

main_list[1] = 'alohomora'
# print(main_list)
# print(my_list)
# print(my_dict)

print(my_list)


# comparison, equality, truth

num = 5
number = 5
print(num == number, num is number)

magic_list = [1, 2, 4]
super_list = [1, 2, 4]
print(magic_list == super_list, magic_list is super_list)

S1 = 'spam'
S2 = 'spam'
print(S1 == S2, S1 is S2)

S3 = 'a longer string'
S4 = 'a longer string'
print(S3 == S4, S3 is S4)

L1 = [1, ('a', 3)]
L2 = [1, ('a', 2)]
print(L1 < L2, L1 == L2, L1 > L2)

print('abc' < 'ac')

D1 = {'a': 1, 'b': 2}
D2 = {'a': 1, 'b': 3}
print(D1 == D2)
print(D1 < D2)


# True and False

if not '':
    print('hi')

print([None] * 10)

print(bool('asd'))
print(bool(''))
print(bool(1))
print(bool(0))
print(bool([]))

print(type([1]) == type([]))
print(type([1]) == list)
print(isinstance([1], list))
print(isinstance('jkk', list))
print(isinstance('jkk', str))

cool_list = ['alina', 'malina']
cool_list.append(cool_list)
print(cool_list)

a = (4, 5, 6)
a = (1,) + a[1:]
print(a)