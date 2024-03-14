#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def get_sum(self, a: int, b: int) -> int:
        
       if a == -b:
            return 0
        
       if abs(a) > abs(b):
            a, b = b, a
            
       if a < 0:
            return - get_sum(-a, -b)
        
       while b:
            
            c = a & b
            a, b = a ^ b, c << 1
            
       return a
