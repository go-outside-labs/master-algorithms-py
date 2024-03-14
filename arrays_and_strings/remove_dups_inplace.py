#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein



def remove_duplicates(nums: list[int]) -> int:
        
        arr_i, dup_i = 0, 1
        
        while arr_i < len(nums) and dup_i < len(nums):
        
            if nums[arr_i] == nums[dup_i]:
                dup_i += 1

            else:
                arr_i += 1
                nums[arr_i] = nums[dup_i]
        
        for i in range(arr_i + 1, dup_i):
            nums[i] = '_'
        
        return  dup_i - arr_i - 1, nums
            
