#!/usr/bin/python3
# 5-no_c.py


def no_c(my_string):
    """
    Remove all characters c and C from a string.
    """
    copy_list = [elem for elem in my_string if elem != 'c' and elem != 'C']
    return ("".join(copy_list))
