#!/usr/bin/python3
# 102-magic_calculation.py


def magic_calculation(a, b):
    """Magic Calculation"""
    output = 0
    for value in range(1, 3):
        try:
            if value > a:
                raise Exception('Too far')
            else:
                output += a ** b / value
        except:
            output = b + a
            break
    return (output)
