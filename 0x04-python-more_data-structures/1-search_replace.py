#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is not None:
        return [item if item != search else replace for item in my_list]
    return None
