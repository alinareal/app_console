import os


class Processing(object):

    def __init__(self, file_path):
        self.file_path = file_path

    def check_path(self):
        if os.path.exists(self.file_path):
            print 'Start processing:'
        else:
            raise OSError('File does not exist at {}.'.format(self.file_path))

    def process_file(self):
        self.check_path()
        if os.stat(self.file_path).st_size == 0:
            print 'File located in the path {} is empty.'.format(self.file_path)

        with open(self.file_path, 'r') as file_name:
            for index, line in enumerate(file_name, start=1):
                print 'String {}:  {}'.format(str(index), line)
