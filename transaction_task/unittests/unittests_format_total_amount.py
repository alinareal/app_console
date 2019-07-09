import unittest

from file_writer import FileWriter

calc_obj = FileWriter('1')


class TestFormatTotalAmount(unittest.TestCase):
    def test1(self):
        self.assertEqual(-13.0, calc_obj.calc([0.0, 13.0, '-']))