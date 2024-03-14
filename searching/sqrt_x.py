#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def sqrt(x) -> int:
    
        if x < 2:
            return x
        
        left, right = 2, x // 2
        
        while left <= right:
            
            mid = (right + left) // 2
            num = mid * mid
            
            if num > x:
                right = mid - 1
                
            elif num < x:
                left = mid + 1
                
            else:
                return mid
            
        return right
