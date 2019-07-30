import argparse
import sys
from sys import argv

from file_writer import FileWriter
from file_reader import FileReader

main_menu = {'1': 'Write to file',
             '2': 'Read from file',
             '0': 'Exit program'}

write_menu = {'1': 'Set header',
              '2': 'Add transaction',
              '3': 'Set transaction',
              '4': 'Create file',
              '5': 'Back'}

header_menu = {'1': 'Set name',
               '2': 'Set surname',
               '3': 'Set patronymic',
               '4': 'Set address',
               '5': 'Back'}

trans_menu = {'1': 'Set transaction sum',
              '2': 'Set currency code',
              '3': 'Back'}

read_menu = {'1': 'Add file path', 
             '2': 'Choose field',
             '3': 'Back'}

field_menu = {'1': 'name',
              '2': 'surname',
              '3': 'patronymic',
              '4': 'address',
              '5': 'transaction sum',
              '6': 'currency code',
              '7': 'transaction number',
              '8': 'transaction amount',
              '9': 'back'}


def print_ordered_menu(our_dict):
    options = our_dict.keys()
    options.sort()
    for entry in options:
        print entry, our_dict[entry]


def create_parser():
    parser_ = argparse.ArgumentParser(description='Process command line file_path.')
    return parser_

if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args(argv[1:])
    write_obj = FileWriter()
    read_obj = FileReader()

    print_ordered_menu(main_menu)
    choice = raw_input('Please select: ')
    if choice == '1':  # write to file
        print_ordered_menu(write_menu)
        choice = raw_input('Please select: ')
        if choice == '1':  # set header
            print_ordered_menu(header_menu)
            choice = raw_input('Please select: ')
            if choice == '1':  # set name
                user_name = raw_input("Enter name: ")
                write_obj.set_header('name', user_name)
            elif choice == '2':  # set surname
                user_surname = raw_input("Enter surname: ")
                write_obj.set_header('surname', user_surname)
            elif choice == '3':  # set patronymic
                user_patr = raw_input("Enter patronymic: ")
                write_obj.set_header('patronymic', user_patr)
            elif choice == '4':  # set address
                user_address = raw_input("Enter address: ")
                write_obj.set_header('address', user_address)
            elif choice == '5':  # back
                print_ordered_menu(write_menu)
            else:
                print('Unknown option selected!')
        elif choice == '2':  # add transaction
            pass
        elif choice == '3':  # set transaction
            if choice == '1':  # set transaction sum
                user_trans_sum = raw_input('Enter transaction sum: ')
                write_obj.set_trans('trans_sum', user_trans_sum)
            elif choice == '2':  # set currency code
                user_currency_code = raw_input('Enter currency code: ')
                write_obj.set_trans('trans_sum', user_currency_code)
            elif choice == '3':  # back
                print_ordered_menu(write_menu)
            else:
                print('Unknown option selected!')
        elif choice == '4':  # create file
            write_obj.create_file()
        elif choice == '5':  # back
            print_ordered_menu(write_menu)
        else:
            print('Unknown option selected!')
    elif choice == '2':  # read from file
        print_ordered_menu(read_menu)
        choice = raw_input('Please select: ')
        if choice == '1':  # add file path
            user_folder = raw_input('Enter folder: ')
            user_file_name = raw_input('Enter file name: ')
            read_obj.set_file_path(user_folder, user_file_name)
            read_obj.read_file()
        elif choice == '2':  # choose field
            print_ordered_menu(field_menu)
            choice = raw_input('Please select: ')
            if choice == '1':
                print(read_obj.header.name)
            elif choice == '2':
                print(read_obj.header.surname)
            elif choice == '3':
                print(read_obj.header.patronymic)
            elif choice == '4':
                print(read_obj.header.address)
            elif choice == '5':
                n = raw_input('Enter transaction counter: ')
                print(read_obj.trans_list[int(n)-1].trans_sum)
            elif choice == '6':
                n = raw_input('Enter transaction counter: ')
                print(read_obj.trans_list[int(n)-1].currency_code)
            elif choice == '7':
                print(read_obj.trailer.trailer_trans_number)
            elif choice == '8':
                print(read_obj.trailer.trailer_trans_amount)
            elif choice == '9':
                print_ordered_menu(read_menu)
        elif choice == '3':  # back
            print_ordered_menu(main_menu)
    elif choice == '0':  # exit program
        sys.exit()
    else:
        print('Unknown option selected!')
