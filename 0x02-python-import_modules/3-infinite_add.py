#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print("{:d}".format(sum(int(n) for n in sys.argv[1:])))
