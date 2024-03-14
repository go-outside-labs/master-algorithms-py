#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def get_next(n):
  
  total_sum = 0
  while n > 0:
    n, digit = divmod(n, 10)
    total_sum += digit**2

  return total_sum


def is_happy(self, n: int) -> bool:

  seen = set()
  while n != 1 and n not in seen:
    seen.add(n)
    n = get_next(n)

  return n == 1
    
