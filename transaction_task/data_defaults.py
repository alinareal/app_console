from collections import OrderedDict

HEADER_DEFAULTS = OrderedDict([('header_id', '01'),
                               ('name', 'John'),
                               ('surname', 'Lennon'),
                               ('patronymic', 'Ivanovich'),
                               ('address', 'Simona9/23MinskBelarus')])

TRANSACTION_DEFAULTS = OrderedDict([('trans_id', '02'),
                                    ('trans_counter', '000001'),
                                    ('trans_sum', '000000002000'),
                                    ('currency_code', '123'),
                                    ('trans_filler', ' ' * 87)])

TRAILER_DEFAULTS = OrderedDict([('trailer_id', '03'),
                                ('trailer_filler', ' ' * 100)])

