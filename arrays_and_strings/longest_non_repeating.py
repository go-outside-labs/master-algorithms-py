#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def length_longest_substring(s) -> int:
        
        result = ""
        this_longest_string = ""
        i = 0
        
        for c in s:
            j = 0
        
            while j < len(this_longest_string):
                
                if c == this_longest_string[j]:
                    if len(this_longest_string) > len(result):
                        result = this_longest_string
                    this_longest_string = this_longest_string[j+1:]
                    
                j += 1
            
            this_longest_string += c
            
        return result, this_longest_string
        
