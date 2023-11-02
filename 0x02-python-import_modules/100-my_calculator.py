#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

ops = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}

if __name__ != "__main__":
    exit(0)

argc = len(sys.argv) - 1
if (argc != 3):
    print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
    sys.exit(1)
a = int(sys.argv[1])
operator = sys.argv[2]
b = int(sys.argv[3])

if operator not in ['+', '-', '*', '/']:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

print("{} {} {} = {}".format(a, operator, b, ops[operator](a, b)))
