#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def convert_sorted_array_to_bst(nums):

      def helper(left, right):
        
            if left > right:
                return None

            p = (left + right) // 2

            root = Node(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)

            return root
        
      return helper(0, len(nums) - 1)
  
