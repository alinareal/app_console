from collections import OrderedDict
from collections import namedtuple

STRUCT = namedtuple('STRUCT', 'POS MAX_LEN')

STRUCT_HEADER = namedtuple('STRUCT_HEADER', 'header_id name surname patronymic address')

ID = STRUCT(slice(0, 2), 2)

NAME = STRUCT(slice(2, 30), 28)
SURNAME = STRUCT(slice(30, 60), 30)

PATRONYMIC = STRUCT(slice(60, 90), 30)
ADDRESS = STRUCT(slice(90, 120), 30)

HEADER_DEFAULTS = OrderedDict([('header_id', '01'),
                               ('name', 'John'),
                               ('surname', 'Lennon'),
                               ('patronymic', 'Ivanovich'),
                               ('address', 'Simona9/23MinskBelarus')])


# result = ''
# for item, max_len in HEADER_DEFAULTS.values(), STRUCT:
#     result += ' ' * (item.MAX_LEN - len(item)) + item
#
# print(result)


valuesList = [HEADER_DEFAULTS['header_id'].rjust(ID.MAX_LEN),
              HEADER_DEFAULTS]


result = HEADER_DEFAULTS['name'].rjust(NAME.MAX_LEN)
print(result)
