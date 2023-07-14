#!/usr/bin/python3
def main():
    a = 10
    b = 5
    import calculator_1
    print("{:d} + {:d} = {:d}".format(a, b, calculator.add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, calculator.sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, calculator.mul(a, b)))
    print("{:d} / {:d} = {:.2f}".format(a, b, calculator.div(a, b)))


if __name__ == "__main__":
    main()
