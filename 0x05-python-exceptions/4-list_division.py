#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    mode = []
    for i in range(list_length):
        le = 0
        try:
            le = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            mode.append(le)
    return mode
