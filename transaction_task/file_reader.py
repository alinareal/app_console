import os

from decimal import Decimal

import config as conf
from models import (Header, Transaction, Trailer)


class FileReader(object):

    def __init__(self):
        self.infile_name = os.path.join('data', 'magic_summer.txt')
        self.header = Header()
        self.trailer = Trailer()
        self.trans_list = []

    def set_file_path(self, folder, file_name):
        self.infile_name = os.path.join(folder, file_name)

    def _check_path(self):  # +
        if os.path.exists(self.infile_name):
            print('Start reading:')
        else:
            raise ValueError('File does not exist at path {}.'.format(self.infile_name))

    def _check_size(self):  # +
        if os.stat(self.infile_name).st_size == 0:
            print('File located in the path {} is empty.'.format(self.infile_name))

    @staticmethod
    def _check_header_pos(header_line):
        if header_line[conf.ID.POS] != conf.HEADER_ID:
            raise ValueError('There is no header on the first line of the file!')

    @staticmethod
    def _check_trans_pos(trans_line):
        if trans_line[conf.ID.POS] != conf.TRANS_ID:
            raise ValueError('There is no transaction on the second line of the file!')

    @staticmethod
    def _check_trailer_pos(trailer_line):
        if trailer_line[conf.ID.POS] != conf.TRAILER_ID:
            raise ValueError('There is no trailer on the last line of the file!')

    def _check_structure(self, lines_list):
        self._check_header_pos(lines_list[0])
        self._check_trans_pos(lines_list[1])
        self._check_trailer_pos(lines_list[-1])

    @staticmethod
    def _strip_spaces(line, pos):   # +
        return line[pos].lstrip()

    @staticmethod
    def _strip_zeroes(line, pos):  # +
        return line[pos].lstrip('0')

    @staticmethod  # +
    def _format_decimal(trans_sum_field):
        try:
            return (Decimal(trans_sum_field) / Decimal('100')).quantize(Decimal('1.00'))
        except:
            raise TypeError('The field has incorrect symbols!')

    def _fill_header(self, line):
        self.header.name = self._strip_spaces(line, conf.NAME.POS)
        self.header.surname = self._strip_spaces(line, conf.SURNAME.POS)
        self.header.patronymic = self._strip_spaces(line, conf.PATRONYMIC.POS)
        self.header.address = self._strip_spaces(line, conf.ADDRESS.POS)

    def _fill_trans(self, line):
        trans = Transaction()
        trans.trans_counter = self._strip_zeroes(line, conf.TRANS_COUNTER.POS)
        trans.trans_sum = self._format_decimal(self._strip_zeroes(line, conf.TRANS_SUM.POS))
        trans.currency_code = self._strip_zeroes(line, conf.CURRENCY_CODE.POS)
        self.trans_list.append(trans)

    def _fill_trailer(self, line):
        self.trailer.trailer_trans_number = self._strip_zeroes(line, conf.TRAILER_TRANS_NUMBER.POS)
        self.trailer.trailer_trans_amount = self._format_decimal(self._strip_zeroes(line,
                                                                                    conf.TRAILER_TRANS_AMOUNT.POS))

    def read_file(self):
        self._check_path()
        self._check_size()

        message = 'File contains line number {} with incorrect ID: {}!'

        with open(self.infile_name, 'r') as file_name:
            lines_list = file_name.readlines()

            self._check_structure(lines_list)

            was_header = False
            was_trailer = False

            for line in lines_list:
                if line[conf.ID.POS] == conf.HEADER_ID:
                    if not was_header:
                        was_header = True
                        self._fill_header(line)
                    else:
                        raise ValueError('The file contains more than one header!')
                elif line[conf.ID.POS] == conf.TRANS_ID:
                    self._fill_trans(line)
                elif line[conf.ID.POS] == conf.TRAILER_ID:
                    if not was_trailer:
                        was_trailer = True
                        self._fill_trailer(line)
                    else:
                        raise ValueError('The file contains more than one trailer!')
                else:
                    for index, line_id in enumerate(file_name, start=1):
                        raise ValueError(message.format(str(index), line_id=conf.ID.POS))
            print('Reading file was completed successfully.')

dog = FileReader()
dog.set_file_path('data', 'magic_summer.txt')
dog.read_file()
print(dog.header.name)
print(dog.header.surname)
print(dog.header.patronymic)
print(dog.header.address)

print(dog.trans_list[0].trans_counter)
print(dog.trans_list[0].trans_sum)
print(dog.trans_list[0].currency_code)

print(dog.trans_list[1].trans_counter)
print(dog.trans_list[1].trans_sum)
print(dog.trans_list[1].currency_code)

print(dog.trans_list[4].trans_counter)
print(dog.trans_list[4].trans_sum)
print(dog.trans_list[4].currency_code)

print(dog.trailer.trailer_trans_number)
print(dog.trailer.trailer_trans_amount)
