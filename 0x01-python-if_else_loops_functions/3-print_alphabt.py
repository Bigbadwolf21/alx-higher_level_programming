#!/usr/bin/python3
"""
Print the ASCII Alphabet in lowercase with letter e and q
"""
for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")
