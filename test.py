"""License information goes here"""

import sys

def basic_print_function(print_str):
    """
        Print string provided by the user, exit if None is provided

        :param print_str: String to be printed to the console
        :return: Nothing
    """
    if print_str is not None:
        print("Hello, {}".format(print_str))
    else:
        print("Exiting, no string provided")
        sys.exit(0)

if __name__ == "__main__":
    basic_print_function("World")
