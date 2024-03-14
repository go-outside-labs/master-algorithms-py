#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def permutations(string) -> list:

    if len(string) == 1:
        return [string]
    
    result = []
    for i, char in enumerate(string):
        for perm in permutation(string[:i] + string[i+1:]):
            result += [char + perm]
    
    return result
