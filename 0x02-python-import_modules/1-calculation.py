#!/usr/bin/python3
a = 10
b = 5
calculator = __import__('calculator_1')
print("{:d} + {:d} = {:d}".format(a, b, calculator.add(a, b)))
print("{:d} - {:d} = {:d}".format(a, b, calculator.sub(a, b)))
print("{:d} * {:d} = {:d}".format(a, b, calculator.mul(a, b)))
print("{:d} / {:d} = {:.0f}".format(a, b, calculator.div(a, b)))
