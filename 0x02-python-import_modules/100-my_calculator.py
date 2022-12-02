#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as extra
    import sys
argNum = len(sys.argv)  # gets number of arguments
la = sys.argv  # stores arguments return by sys module
if argNum != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
else:
    a = int(la[1])
    b = int(la[3])
    if la[2] == "-":
        print("{:d} - {:d} = {:d}".format(a, b, extra.sub(a, b)))
    elif la[2] == "*":
        print("{:d} * {:d} = {:d}".format(a, b, extra.mul(a, b)))
    elif la[2] == "/":
        print("{:d} / {:d} = {:d}".format(a, b, extra.div(a, b)))
    elif la[2] == "+":
        print("{:d} + {:d} = {:d}".format(a, b, extra.add(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
