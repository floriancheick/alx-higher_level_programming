#!/usr/bin/python3
if __name__ == "__main__":
    import sys
value = sys.argv
number = len(value)
i = 1
if number == 1:
    print("0 arguments.")
elif number == 2:
    print("1 argument:")
    print("1: {}".format(value[1]))
elif number > 2:
    print("{:d} arguments:".format(number-1))
    while i < number:
        print("{:d}: {}".format((i), value[i]))
        i = i + 1
        
