from collections import namedtuple
from config import (HEADER_ID, TRANS_ID, TRAILER_ID)

STRUCT_HEADER = namedtuple('STRUCT_HEADER', 'HEADER_ID NAME SURNAME PATRONYMIC ADDRESS')
STRUCT_TRANSACTION = namedtuple('STRUCT_TRANSACTION', 'TRANS_ID TRANS_COUNTER TRANS_SUM CURRENCY_CODE TRANS_FILLER')
STRUCT_TRAILER = namedtuple('STRUCT_TRAILER', 'TRAILER_ID TRAILER_TRANS_NUMBER TRAILER_TRANS_AMOUNT TRAILER_FILLER')


class Header(object):
    def __init__(self):
        self.header_id = HEADER_ID
        self.name = ''
        self.surname = ''
        self.patronymic = ''
        self.address = ''


class Transaction(object):
    def __init__(self):
        self.trans_id = TRANS_ID
        self.trans_counter = ''
        self.trans_sum = ''
        self.currency_code = ''
        self.trans_filler = ''


class Trailer(object):
    def __init__(self):
        self.trailer_id = TRAILER_ID
        self.trailer_trans_number = ''
        self.trailer_trans_amount = ''
        self.trailer_filler = ''
