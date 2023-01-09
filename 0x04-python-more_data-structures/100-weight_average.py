#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    num = 0
    den = 0
    for top in my_list:
        num += top[0] * top[1]
        den += top[1]
        return (num / den)
