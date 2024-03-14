#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def convert_to_any_base(base: int, num: int) -> str:
        
        if num == 0:
            return "0"
    
        n = abs(num)
        result = ""
        
        while n:
            result += str(n % base)
            n //= base
        
        if num < 0: 
            result += '-'
            
        return  result[::-1]
