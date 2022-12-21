#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        return fct(*args)
    except (ZeroDivisionError, IndexError, TypeError, ValueError) as err:
        stderr.write("Exception: {}\n".format(err))
        return None
