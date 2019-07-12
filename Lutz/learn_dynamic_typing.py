import sys

my_list = [3, 2, 8]
his_list = my_list
my_list[1] = 4
print(my_list)
print(his_list)

print(my_list == his_list)
print(my_list is his_list)


my_list = [3, 2, 8]
his_list = my_list[:]

print(my_list == his_list)
print(my_list is his_list)

my_list[1] = 4
print(my_list)
print(his_list)

print(my_list == his_list)
print(my_list is his_list)


X = 42
Y = 42
print(X == Y)
print(X is Y)

print(sys.getrefcount(0))
print(sys.getrefcount(1))
print(sys.getrefcount(2))
print(sys.getrefcount(3))
print(sys.getrefcount(4))
print(sys.getrefcount(5))
print(sys.getrefcount(6))
print(sys.getrefcount(7))
print(sys.getrefcount(8))
print(sys.getrefcount(9))
print(sys.getrefcount(10))

# 1
A = 'spam'
B = A
B = 'shrubbery'

print(A)

# 2
A = ['spam']
B = A
B[0] = 'shrubbery'

print(A)

# 3
A = ['spam']
B = A[:]
B[0] = 'shrubbery'

print(A)
