from collections import namedtuple

Player = namedtuple('Player', 'surname rank country')

barti = Player(surname='Barti', rank=1, country='Australia')
kvitova = Player('Kvitova', 9, 'Czechia')

# print(barti)
# print(kvitova)
#
# print(barti.surname)
# print(kvitova.country)

# for p in [barti, kvitova]:
#     print p
#     print '%s is a player ranked %d from %s' % p

for i in [barti, kvitova]:
    print '{} is a player ranked {} from {}'.format(i)
