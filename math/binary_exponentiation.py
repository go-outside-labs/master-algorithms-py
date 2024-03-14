#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

'''
Binary exponentiation, also known as exponentiation by squaring, is a technique for 
efficiently computing the power of a number. By repeatedly squaring x and halving n, 
we can quickly compute x^n using a logarithmic number of multiplications.
'''

def binary_exp(x: float, n: int) -> float:

  if n == 0:
      return 1

  if n < 0:
      return 1.0 / binary_exp(x, -1 * n)
        
  if n % 2 == 1:
      return x * binary_exp(x * x, (n - 1) // 2)
        
  return binary_exp(x * x, n // 2)
