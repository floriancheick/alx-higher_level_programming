#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    idex = 0
    while idex < x:
        try:
            print("{}".format(my_list[idex]), end='')
        except IndexError:
            break
        idex += 1
    print()
    return
