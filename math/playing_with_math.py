#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


import math
import random


def find_greatest_common_divider(a, b) -> int:
    
    while(b != 0):
        result = b
        a, b = b, a % b
        
    return result


def _is_prime(number) -> bool:

    if number < 2:
        return False

    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            return False
    
    return True


def find_prime_factors(number) -> list:
    
    divisors = [d for d in range(2, number//2 + 1) if number % d == 0]
    primes = [d for d in divisors if _is_prime(d)]

    return primes
