#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

# A peak element is an element that is strictly greater than its neighbors.

def peak_element(nums):

        left, right = 0, len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            if nums[mid + 1] < nums[mid]:
                right = mid
            else:
                left = mid + 1

        return left
  
