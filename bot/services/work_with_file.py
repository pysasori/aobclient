import os


def write_to_file(number, filename):
    with open(filename, 'w') as file:
        file.write(str(number))


def read_from_file(filename) -> str:
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.read()



