#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def merge_sort(array):

    # part 1: recursively divide the array into subarrays
    if len(array) < 2:
        return array
    
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    # part 2: merge the subarrays
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1
    
    if left[i:]:
        result.extend(left[i:])
    if right[j:]:
        result.extend(right[j:])
    
    return result
  
