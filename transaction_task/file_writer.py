from decimal import Decimal, getcontext

from data_defaults import (HEADER_DEF, TRANS_DEF, TRAILER_DEF)
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
        header_values_list = [HEADER_DEF['header_id'].rjust(conf.ID.MAX_LEN),
                              HEADER_DEF['name'].rjust(conf.NAME.MAX_LEN),
                              HEADER_DEF['surname'].rjust(conf.SURNAME.MAX_LEN),
                              HEADER_DEF['patronymic'].rjust(conf.PATRONYMIC.MAX_LEN),
                              HEADER_DEF['address'].rjust(conf.ADDRESS.MAX_LEN),
                              conf.LINE_ENDING
                              ]
        return ''.join(header_values_list)

    def create_trans(self):
        self._process_trans_counter_and_total_amount()
        trans_values_list = [TRANS_DEF['trans_id'].rjust(conf.ID.MAX_LEN),
                             TRANS_DEF['trans_counter'].rjust(conf.TRANS_COUNTER.MAX_LEN),
                             TRANS_DEF['trans_sum'].rjust(conf.TRANS_SUM.MAX_LEN),
                             TRANS_DEF['currency_code'].rjust(conf.CURRENCY_CODE.MAX_LEN),
                             TRANS_DEF['trans_filler'].rjust(conf.TRANS_FILLER.MAX_LEN),
                             conf.LINE_ENDING
                             ]

        return ''.join(trans_values_list)

    def create_trailer(self):
        trailer_values_list = [TRAILER_DEF['trailer_id'].rjust(conf.ID.MAX_LEN),
                               str(self.trans_counter).rjust(conf.TRAILER_TRANS_NUMBER.MAX_LEN, '0'),
                               self._format_total_amount(),
                               TRAILER_DEF['trailer_filler'].rjust(conf.TRAILER_FILLER.MAX_LEN),
                               conf.LINE_ENDING
                               ]

        return ''.join(trailer_values_list)

    def _process_trans_counter_and_total_amount(self):
        self.trans_counter += 1
        self.total_amount += Decimal(TRANS_DEF['trans_sum']) / Decimal('100')

    def _format_total_amount(self):
        max_len = conf.TRAILER_TRANS_AMOUNT.MAX_LEN
        total_amount = self.total_amount.quantize(Decimal('1.00'))
        amount_without_dot = str(total_amount).replace('.', '')
        final_amount = amount_without_dot.rjust(max_len, '0')
        return final_amount


cat = FileWriter()
print(cat.create_header())
# print(len(cat.create_header()))
print(cat.create_trans())
# print(len(cat.create_trans()))
print(cat.create_trailer())
cat.create_file()

# (str(self.total_amount).rjust(conf.TRAILER_TRANS_AMOUNT.MAX_LEN, '0')).replace('.', ''),

# a = Decimal('2000.00') / Decimal('100')
# print(a)
# print(type(a))

# print(conf.NAME.MAX_LEN)
