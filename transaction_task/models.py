from config import (HEADER_ID, TRANS_ID, TRAILER_ID)


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
