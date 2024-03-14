#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

# Given a fixed-length integer array arr, duplicate each occurrence of zero, 
# shifting the remaining elements to the right.


def duplicate_zeros(arr: list[int]) -> list[int]:

        i = 0
        while i < len(arr):
            
            if arr[i] == 0 and i != len(arr) - 1:

                range_here = len(arr) - (i + 2)
                while range_here > 0:
                    arr[i + range_here + 1] = arr[i + range_here]
                    range_here -= 1

                arr[i+1] = 0
                i += 2
            
            else:
                i += 1

        return arr
