#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def convert_to_hex(num: int) -> str:
      
  hex_chars  = "0123456789abcdef"
  size = 32
  base = 16
        
  if num == 0:
    return "0"
        
  if num < 1:
    num += 2**size
        
  result = ""
  while num:
    result += hex_chars[num % base]
    num //= base
            
  return result[::-1]
