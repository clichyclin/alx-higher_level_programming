#!/usr/bin/python3
"""
    function that replaces an element of a list at a specific position
    my_list: a list
    idx: a index to list position
    new_element: a new element to add
"""



def replace_in_list(my_list, inx, element):
if 0 <= inx < len(my_list):
my_list[inx] = element

return my_list
