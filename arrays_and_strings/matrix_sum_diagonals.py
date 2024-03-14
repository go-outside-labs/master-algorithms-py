#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

def diagonal_difference(arr):

    diag_1 = 0
    diag_2 = 0
    
    i, j = 0, len(arr) - 1
    
    while i < len(arr) and j >= 0:
        
        diag_1 += arr[i][i]
        diag_2 += arr[i][j]
        i += 1
        j -= 1
        
    return diag_1, diag_2, abs(diag_1 - diag_2)
            
