from collections import namedtuple
from config import (HEADER_ID, TRANS_ID, TRAILER_ID)

STRUCT_HEADER = namedtuple('STRUCT_HEADER', 'header_id name surname patronymic address')
STRUCT_TRANSACTION = namedtuple('STRUCT_TRANSACTION', 'trans_id trans_counter trans_sum currency_code trans_filler')
STRUCT_TRAILER = namedtuple('STRUCT_TRAILER', 'trailer_id trailer_trans_number trailer_trans_amount trailer_filler')


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
