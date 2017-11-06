''' 

Implement a calculator for simple arithmetic expressions in revese polish 
notation. (4 points)

The reverse polish notation notation 

Reverse Polish notation (RPN) is a mathematical notation in which every
operator follows all of its operands. It is also known as postfix
notation and does not need any parentheses as long as each operator has a fixed
number of operands. For instance, the expression

    5 + ((1 + 2) * 4) − 3

is written in RPM as

    5 1 2 + 4 * + 3 −

(see Wikipedia for more details.)

Algorithm:

Datastructure: A stack (list) which stores the operands

while there are input tokens left
    read the next token from input.
    if the token is a value
        push (append) it onto the stack.
    otherwise, the token must be an operator (+, -, *, /)
        pop (remove) the last two operators from the stack
        apply the operator to these two values
        push the result to the stack

When applied to well-formed input, the stack will contain a single value
at the end.

NOTE: 

Your implementation shoul raise an ArithmeticException when the function is
applied to a string which is not a well-formed expression. For instance,

$ python3 calc.py "5 1 2 + 4 * + 3 −"
14

$ python3 calc.py '5 1 2 + 4 * + 3'
Invalid input

$ python3 calc.py '5 + 2'
Invalid input

'''

import sys


def calc(tokens):
    result = 0
    stack = []
    operators = ['+', '-', '*', '/']
    while len(tokens) > 0:
        current = tokens.pop(0)
        if current not in operators:
            stack.append(current)
        else:
            if len(stack) < 2:
                raise ArithmeticError

            first = stack.pop()
            second = stack.pop()

            if first in operators or second in operators:
                raise ArithmeticError

            mathString = second + current + first
            result = str(eval(mathString))
            stack.append(result)

    if len(stack) > 1:
        raise ArithmeticError

    return result


def main():
    try:
        print(calc(sys.argv[1].split()))
    except ArithmeticError:
        print('Invalid input')

if __name__ == '__main__':
    main()
