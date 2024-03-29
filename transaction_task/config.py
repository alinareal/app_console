import os
import uuid
from collections import namedtuple

STRUCT = namedtuple('STRUCT', 'POS MAX_LEN')

INFILE_NAME = os.path.join('data', 'File.{}.txt'.format(str(uuid.uuid4())))
# INFILE_NAME = os.path.join('data', 'magic_summer.txt')

LINE_LEN = 120
LINE_ENDING = '\n'

HEADER_ID = '01'
TRANS_ID = '02'
TRAILER_ID = '03'

ID = STRUCT(slice(0, 2), 2)

NAME = STRUCT(slice(2, 30), 28)
SURNAME = STRUCT(slice(30, 60), 30)
PATRONYMIC = STRUCT(slice(60, 90), 30)
ADDRESS = STRUCT(slice(90, 120), 30)

TRANS_COUNTER = STRUCT(slice(2, 8), 6)
TRANS_SUM = STRUCT(slice(8, 20), 12)
CURRENCY_CODE = STRUCT(slice(20, 23), 3)
TRANS_FILLER = STRUCT(slice(23, 120), 97)

TRAILER_TRANS_NUMBER = STRUCT(slice(2, 8), 6)
TRAILER_TRANS_AMOUNT = STRUCT(slice(8, 20), 12)
TRAILER_FILLER = STRUCT(slice(20, 120), 100)

# NOT_ALLOWED_FIELDS_TO_SET = ('header_id', 'trans_id', )
ALLOWED_FIELDS_TO_SET = ('name', 'surname', 'patronymic', 'address', 'trans_sum', 'currency_code')
