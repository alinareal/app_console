from decimal import Decimal

from data_defaults import (HEADER_DEF, TRANS_DEF, TRAILER_DEF)
import config as conf


class FileWriter(object):
    def __init__(self):
        self.trans_counter = 0
        self.total_amount = Decimal()
        self.trans_list = []
        self.header_def_copy = HEADER_DEF.copy()
        self.trans_def_copy = TRANS_DEF.copy()

    def create_file(self):
        """
        Creates file and writes there header, transactions and trailer

        :return: None
        """
        with open(conf.INFILE_NAME, 'w') as infile_name:
            infile_name.write(self.create_header())
            for trans in self.create_trans():
                infile_name.write(trans)
            infile_name.write(self.create_trailer())

    def set_header(self, key, value):
        self.header_def_copy[key] = value

    def create_header(self):
        """
        Creates a header string from header fields

        :return: ''.join(header_values_list) (str)
        """
        header_values_list = [self.header_def_copy['header_id'].rjust(conf.ID.MAX_LEN),
                              self.header_def_copy['name'].rjust(conf.NAME.MAX_LEN),
                              self.header_def_copy['surname'].rjust(conf.SURNAME.MAX_LEN),
                              self.header_def_copy['patronymic'].rjust(conf.PATRONYMIC.MAX_LEN),
                              self.header_def_copy['address'].rjust(conf.ADDRESS.MAX_LEN),
                              conf.LINE_ENDING
                              ]
        header_str = ''.join(header_values_list)

        if len(header_str) > 121:
            raise ValueError('The length of your string is more than allowed!')

        return header_str

    def set_trans(self, key, value):
        try:
            self.trans_list[-1][key] = value
        except:
            raise IndexError('First add transaction, then set values.')

    def create_trans(self):
        """
        Creates a transaction string from transaction fields

        :return: ''.join(trans_values_list) (str)
        """
        trans_list = []
        for transactionDict in self.trans_list:
            self.total_amount += Decimal(transactionDict['trans_sum']) / Decimal('100')
            trans_values_list = [transactionDict['trans_id'].rjust(conf.ID.MAX_LEN),
                                 transactionDict['trans_counter'].rjust(conf.TRANS_COUNTER.MAX_LEN),
                                 transactionDict['trans_sum'].rjust(conf.TRANS_SUM.MAX_LEN),
                                 transactionDict['currency_code'].rjust(conf.CURRENCY_CODE.MAX_LEN),
                                 transactionDict['trans_filler'].rjust(conf.TRANS_FILLER.MAX_LEN),
                                 conf.LINE_ENDING
                                 ]
            trans_list.append(''.join(trans_values_list))
        # if len(''.join(trans_values_list)) > 121:
        #     raise ValueError('The length of your string is more than allowed!')
        return trans_list

    def create_trailer(self):
        """
        Creates a trailer string from trailer fields

        :return: ''.join(trailer_values_list) (str)
        """
        trailer_values_list = [TRAILER_DEF['trailer_id'].rjust(conf.ID.MAX_LEN),
                               str(self.trans_counter).rjust(conf.TRAILER_TRANS_NUMBER.MAX_LEN, '0'),
                               self._format_total_amount(),
                               TRAILER_DEF['trailer_filler'].rjust(conf.TRAILER_FILLER.MAX_LEN),
                               conf.LINE_ENDING
                               ]

        return ''.join(trailer_values_list)

    def _format_total_amount(self):
        """
        Brings total_amount to the appropriate view

        :return: final_amount (str)
        """
        max_len = conf.TRAILER_TRANS_AMOUNT.MAX_LEN
        total_amount = self.total_amount.quantize(Decimal('1.00'))
        amount_without_dot = str(total_amount).replace('.', '')
        final_amount = amount_without_dot.rjust(max_len, '0')
        return final_amount

    def add_trans(self):
        """
        Adds the transaction to the list with transactions

        :return: None
        """
        self.trans_counter += 1
        trans_def_copy = TRANS_DEF.copy()
        self.trans_list.append(trans_def_copy)

    # def _check_len_header(self):
        # ...

    # def _check_len_trans(self):
    #     ...

cat = FileWriter()
cat.set_header('name', 'Alina')
cat.set_header('surname', 'Laevskaya')
cat.set_header('patronymic', 'Anatolievna')
# cat.set_header('patronymic', 'Anatolievnammmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')
cat.create_header()

cat.add_trans()
cat.set_trans('trans_sum', '000000003000')
cat.set_trans('currency_code', '124')

cat.add_trans()
cat.set_trans('currency_code', '125')


cat.add_trans()
cat.add_trans()

cat.create_trailer()
cat.create_file()

# TODO: if the len of the string is longer than needed
