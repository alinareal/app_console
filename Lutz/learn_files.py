good_file = open('alina.txt', 'w')
good_file.write('Abracadabra\n')
good_file.write('Abracadabra you\n')
good_file.write('Abracadabra you and me\n')
good_file.close()

good_file = open('alina.txt')
# print(good_file.read())
# print(good_file.readline())
# print(good_file.readline())
# print(good_file.readline())

for line in good_file:
    print(line)

age, code, phone = 12, 03, 8548933
name = 'Durian'
jobs = ['barista', 'pizza maker']
family = {'daughter': 'Alla', 'son': 'Mark'}

his_file = open('durian.txt', 'w')
his_file.write('{},{},{}\n'.format(str(age), str(code), str(phone)))
his_file.write(name + '\n')
his_file.write(str(jobs) + '\n')
his_file.write(str(family) + '\n')
his_file.close()

her_file = open('durian.txt')
her_nums = her_file.readline().split(',')
print(her_nums)
numbers = [int(i) for i in her_nums]
print(numbers)

her_str = her_file.readline().rstrip()
print(her_str)

her_list = eval(her_file.readline())
print(her_list)
print(type(her_list))

her_dict = eval(her_file.readline())
print(her_dict)
print(type(her_dict))

with open('durian.txt') as my_file:
    for line in my_file:
        print(line)

my_file = open('myfile.txt', 'w')
my_file.write('Hello file world!' + '\n')
my_file.close()

my_file = open('myfile.txt')
print(my_file.read())
my_file.close()