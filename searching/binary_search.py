#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def binary_search_recursive(array, item, higher=None, lower=0):

    higher = higher or len(array)
    
    if higher < lower:
        return False
    
    mid = (higher + lower) // 2
    
    if item == array[mid]:
        return mid
        
    elif item < array[mid]:
        return binary_search_recursive(array, item, mid - 1, lower)
        
    else:
        return binary_search_recursive(array, item, higher, mid + 1)


def binary_search_iterative(array, item):
    
    if lens(nums) == 0:
        return False
        
    lower, higher = 0, len(array)

    while lower < higher:
        mid = (higher + lower) // 2
        
        if array[mid] == item:
            return mid 
            
        elif array[mid] > item:
            higher = mid - 1
            
        else:
            lower = mid + 1
            
    return False


def binary_search_matrix(matrix, item, lower=0, higher=None):

    if not matrix:
        return False
    
    rows = len(matrix)
    cols = len(matrix[0])
    higher = higher or rows * cols

    if higher > lower:
        mid = (higher + lower) // 2
        row = mid // cols
        col = mid % cols

        if item == matrix[row][col]:
            return row, col
        elif item < matrix[row][col]:
            return binary_search_matrix(matrix, item, lower, mid - 1)
        else:
            return binary_search_matrix(matrix, item, mid + 1, higher)
        
    return False
