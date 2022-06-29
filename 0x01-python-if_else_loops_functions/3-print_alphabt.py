#!/usr/bin/python3
"""
Print all the ASCII Alphabets in lower case except e and q
"""
for letter in range(97, 123):
    if chr(letter) is not 'q' and chr(letter) is not 'e':
        print("{}".format(chr(letter)), end="")
