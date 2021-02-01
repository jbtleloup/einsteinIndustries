from tkinter import Tk
from tkinter.filedialog import askopenfilename

# main hashtable, will be used to access the values as needed
TABLE = {}

# utility hashtable to clean boolean-like values
BOOLLIKETABLE = {'yes': True, 'on': True, 'true': True, 'no': False, 'off': False, 'false': False}


def file_input():
    Tk().withdraw()
    return askopenfilename()


def get_user_input():
    return input("-> ")


def read_file(path):
    with open(path) as f:
        for i, l in enumerate(f):
            try:
                wrapper(l)
            except SyntaxError as e:
                print(f"{e} at line {i}... Verify your file")


def isvalid(line):
    # ignore comments and empty line
    if line[0] == '#' or not line.strip():
        return False
    # throw exception if there is no '='
    if '=' not in line:
        raise SyntaxError("it looks like '=' is missing")
    # TODO: add more testing

    return True


def isnumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def cleaning(line):
    # split into key/value pair then remove whitespace
    l = [x.strip() for x in line.split('=')]
    [key, value] = l
    # Boolean-like config values (on/off, yes/no, true/false) should return real booleans: true/false.
    cleanvalue = BOOLLIKETABLE[value] if value in BOOLLIKETABLE else value
    # Numeric config values should return real numerics: integers, doubles, etc
    return key, float(cleanvalue) if isnumber(cleanvalue) else cleanvalue


def add_to_table(key, value):
    TABLE[key] = value


def wrapper(line):
    try:
        if isvalid(line):
            [key, value] = cleaning(line)
            add_to_table(key, value)
    except SyntaxError as e:
        raise


def display_table_value(key):
    try:
        print(TABLE[key])
    except KeyError as e:
        print(f"The key {e} could not be found... Please verify your spelling")


def show_welcome_message():
    print("**********************************************************")
    print("|                                                        |")
    print("|                WELCOME TO AMAZING PARSING              |")
    print("|  author: Jean-Baptiste Tamas-Leloup github: jbtleloup  |")
    print("|                                                        |")
    print("**********************************************************")


def show_table_keys_message():
    print("Please select one of the suggested keys or type exit to quit")
    print(", ".join(list(TABLE.keys())))


def show_thankyou_message():
    print("Thank you for using Amazing parsing!!")


def main():
    show_welcome_message()
    filepath = file_input()
    read_file(filepath)
    key = ""
    print("\n")
    while key != "exit":
        show_table_keys_message()
        key = get_user_input()
        display_table_value(key)
    show_thankyou_message()


if __name__ == '__main__':
    main()
