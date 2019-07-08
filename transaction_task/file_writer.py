from decimal import Decimal

from data_defaults import (HEADER_DEFAULTS, TRANSACTION_DEFAULTS, TRAILER_DEFAULTS)
import config as conf


class FileWriter(object):
    def __init__(self):
        self.trans_counter = 0
        self.total_amount = Decimal()

    def create_file(self):
        with open(conf.INFILE_NAME, 'w') as infile_name:
            infile_name.write(self.create_header())
            infile_name.write(self.create_trans())
            infile_name.write(self.create_trailer())

    def create_header(self):
        header_values_list = [HEADER_DEFAULTS['header_id'].rjust(conf.ID.MAX_LEN),
                              HEADER_DEFAULTS['name'].rjust(conf.NAME.MAX_LEN),
                              HEADER_DEFAULTS['surname'].rjust(conf.SURNAME.MAX_LEN),
                              HEADER_DEFAULTS['patronymic'].rjust(conf.PATRONYMIC.MAX_LEN),
                              HEADER_DEFAULTS['address'].rjust(conf.ADDRESS.MAX_LEN),
                              conf.LINE_ENDING
                              ]
        return ''.join(header_values_list)

    def create_trans(self):
        self.trans_counter += 1
        trans_values_list = [TRANSACTION_DEFAULTS['trans_id'].rjust(conf.ID.MAX_LEN),
                             TRANSACTION_DEFAULTS['trans_counter'].rjust(conf.TRANS_COUNTER.MAX_LEN),
                             TRANSACTION_DEFAULTS['trans_sum'].rjust(conf.TRANS_SUM.MAX_LEN),
                             TRANSACTION_DEFAULTS['currency_code'].rjust(conf.CURRENCY_CODE.MAX_LEN),
                             TRANSACTION_DEFAULTS['trans_filler'].rjust(conf.TRANS_FILLER.MAX_LEN),
                             conf.LINE_ENDING
                             ]

        return ''.join(trans_values_list)

    def create_trailer(self):
        trailer_values_list = [TRAILER_DEFAULTS['trailer_id'].rjust(conf.ID.MAX_LEN),
                               str(self.trans_counter).rjust(conf.TRAILER_TRANS_NUMBER.MAX_LEN, '0'),
                               TRAILER_DEFAULTS['trailer_filler'].rjust(conf.TRAILER_FILLER.MAX_LEN),
                               conf.LINE_ENDING
                               ]

        return ''.join(trailer_values_list)


cat = FileWriter()
print(cat.create_header())
# print(len(cat.create_header()))
print(cat.create_trans())
# print(len(cat.create_trans()))
print(cat.create_trailer())
cat.create_file()










# print(conf.NAME.MAX_LEN)
