#!/usr/bin/python3
# 9-multiple_by_2.py

def multiply_by_2(a_dictionary):
    """Return a new dict with vals multipled by 2."""
    return ({i: a_dictionary[i] * 2 for i in a_dictionary})
