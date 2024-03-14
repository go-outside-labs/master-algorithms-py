#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

"""
Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
"""


def check_if_exist(arr: list[int]) -> bool:
        
        aux_dict = {}
        
        for i, num in enumerate(arr):
            aux_dict[2 * num] = i
        
        for j, num in enumerate(arr):
            if num in aux_dict.keys() and j != aux_dict[num]:
                return (j, aux_dict[num])
                
        
        return False

if __name__ == "__main__":

    arr = [-2, 0, 10, -19, 4, 6, -8]
    print(check_if_exist(arr)) 
