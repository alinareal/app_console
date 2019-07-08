names = ['Hali', 'Sagd', 'Goga']

print list(enumerate(names, start=1))

enumerated_names = list(enumerate(names, start=1))

for number, name in enumerated_names:
    print 'Person {} is {}.'.format(number, name)


