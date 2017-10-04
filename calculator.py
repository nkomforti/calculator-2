"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


while True:
    user_input = raw_input('> ')
    input_tokens = user_input.split(' ')

    if input_tokens[0] == '+':
        add_result = add(float(input_tokens[1]), float(input_tokens[2]))
        print add_result

    if input_tokens[0] == '-':
        sub_result = subtract(float(input_tokens[1]), float(input_tokens[2]))
        print sub_result

    if input_tokens[0] == '*':
        mult_result = multiply(float(input_tokens[1]), float(input_tokens[2]))
        print mult_result

    if input_tokens[0] == '/':
        div_result = divide(float(input_tokens[1]), float(input_tokens[2]))
        print div_result