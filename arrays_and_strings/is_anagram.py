#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def is_anagram(string1, string2) -> bool:

    string1 = string1.lower()
    string2 = string2.lower()

    if len(string1) != len(string2):
        return False

    for c in string1:
        if c not in string2:
            return False
    
    return True
