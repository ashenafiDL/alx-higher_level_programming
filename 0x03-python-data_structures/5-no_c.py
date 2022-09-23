#!/usr/bin/python3
def no_c(my_string):
    new = [c for c in my_string if c not in ['c', 'C']]
    return ("".join(new))
