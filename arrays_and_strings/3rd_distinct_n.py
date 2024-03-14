#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

'''
Given an integer array nums, return the third distinct maximum 
number in this array. If the third maximum does not exist, 
return the maximum number.

Do it O(n).
'''

import math


def third_max(nums: list[int]) -> int:
        
        first_max = -math.inf
        second_max = -math.inf
        third_max = -math.inf
        
        for n in nums:
            
            if n == first_max or n == second_max or n == third_max:
                continue
            elif n > first_max:
                third_max = second_max
                second_max = first_max
                first_max = n
            elif n > second_max:
                third_max = second_max
                second_max = n
            elif n > third_max:
                third_max = n
        
        if third_max == -math.inf:
            third_max = max(second_max, first_max)
                
        return third_max


if __name__ == "__main__":

    nums = [3,2,1]
    assert(third_max(nums) == 1)
