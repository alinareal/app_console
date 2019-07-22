from config import (HEADER_ID, TRANS_ID, TRAILER_ID)


class Header(object):
    __slots__ = ('header_id', 'name', 'surname', 'patronymic', 'address')

    def __init__(self):
        self.header_id = HEADER_ID
        self.name = ''
        self.surname = ''
        self.patronymic = ''
        self.address = ''


class Transaction(object):
    __slots__ = ('trans_id', 'trans_counter', 'trans_sum', 'currency_code', 'trans_filler')

    def __init__(self):
        self.trans_id = TRANS_ID
        self.trans_counter = ''
        self.trans_sum = ''
        self.currency_code = ''
        self.trans_filler = ''


class Trailer(object):
    __slots__ = ('trailer_id', 'trailer_trans_number', 'trailer_trans_amount', 'trailer_filler')

    def __init__(self):
        self.trailer_id = TRAILER_ID
        self.trailer_trans_number = ''
        self.trailer_trans_amount = ''
        self.trailer_filler = ''
