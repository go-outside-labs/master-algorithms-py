#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def is_permutation_of_palindromes(some_string):

    aux_dict = {}

    for c in some_string.strip():

        if c in aux_dict.keys():
            aux_dict[c] -= 1
        else:
            aux_dict[c] = 1
        
    for v in aux_dict.values():
        if  v != 0:
            return False
    
    return True
