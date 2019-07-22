super_list = []
magic_list = [1, 3, 'a', True, 'a']
good_list = [1, [4, 5, [6, 7]]]
bad_list = list('Lemon')
first_list = list(range(4, 8))

print(bad_list)
print(first_list)
print(magic_list[2])
print(good_list[1][2][0])
print(magic_list[1:3])
print(len(good_list))
print(magic_list + good_list)
print(magic_list * 3)

for i in magic_list:
    print('me:' + str(i))

print(1 in magic_list)
print(2 in magic_list)

magic_list.append(6)
print(magic_list)

magic_list.extend([2, 3, 5])
print(magic_list)

magic_list.insert(3, '7')
print(magic_list)

print(magic_list.index(3))

print(magic_list.count('a'))

magic_list.sort()
print(magic_list)
magic_list.reverse()
print(magic_list)

del magic_list[0]
print(magic_list)

magic_list.pop(1)
print(magic_list)

magic_list.remove('a')
print(magic_list)

magic_list[0] = 45
print(magic_list)

magic_list[1:3] = [7, 8]
print(magic_list)

hello_list = [i + 2 for i in range(3, 10)]
print(hello_list)

print(map(abs, [-1, -2, 0, 1, 2]))
print(list(map(abs, [-1, -2, 0, 1, 2])))

L = [1, 2, 3]
L[1:2] = [4, 5]
print(L)

L[1:2] = []
print(L)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list[2:5] = my_list[3:6]
print(my_list)

print(my_list+[4])
print(my_list)

L = ['abc', 'ABD', 'aBe']
L.sort(key=str.lower)
print(L)

L = ['abc', 'ABD', 'aBe']
L.sort(key=str.lower, reverse=True)
print(L)

L = ['a', 'b', 'e']
print(sorted(L, key=str.lower, reverse=True))

his_list = [1, 4, 7, 8]
his_list.reverse()
print(his_list)

print(list(reversed(his_list)))

print(dir(list))
