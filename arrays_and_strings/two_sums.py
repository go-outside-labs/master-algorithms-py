#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def two_sum(nums: list[int], target: int) -> list[int]:
        
  aux_dict = {}
  for i, n in enumerate(nums):
    complement = target - n
            
  if complement in aux_dict:
    return [aux_dict[complement][0], i]
            
  aux_dict[n] = (i, n)
            
