import argparse
from sys import argv

from proc import Processing


def create_parser():
    parser_ = argparse.ArgumentParser(description='Process command line file_path.')
    parser_.add_argument('FILE_PATH', type=str)
    return parser_

if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args(argv[1:])
    py_calc_obj = Processing(namespace.FILE_PATH)
    py_calc_obj.process_file()
