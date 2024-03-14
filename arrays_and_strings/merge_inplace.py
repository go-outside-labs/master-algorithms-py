#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two 
integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, 
but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements 
that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

def merge(big_list: list[int], m: int, small_list: list[int], n: int) -> None:

        index_big, index_small, index_backward = m - 1, n - 1, m + n - 1
        
        while index_big >= 0 and index_small >= 0:
            
            if small_list[index_small] > big_list[index_big]:
                big_list[index_backward] = small_list[index_small]
                index_small -= 1
            else: 
                big_list[index_backward] = big_list[index_big]
                index_big -= 1
        
            index_backward -= 1

        while index_backward >= 0 and index_big >= 0:
            big_list[index_backward] = big_list[index_big]
            index_backward -= 1
            index_big -= 1
        
        while index_backward >= 0 and index_small >= 0:
            big_list[index_backward] = small_list[index_small]
            index_backward -= 1
            index_small -= 1
