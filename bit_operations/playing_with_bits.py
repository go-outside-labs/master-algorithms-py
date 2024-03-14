#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def set_bit(num, i):
    mask = 1 << i
    return bin( num | mask )

def update_bit(num, i, v):
    mask = ~ (1 << i)
    return bin( (num & mask) | (v << i) )

def count_bits_swapped(a, b):
    count = 0
    m = a^b
    while m:
        count +=1
        m = m & (m-1)
    return count

def clear_bit(num, i):
    mask = ~ (1 << i)   # -0b10001
    return bin(num & mask)

def swap_bit_in_place(a, b):
    a = a^b
    b = a^b
    a = a^b
    return a, b

def find_how_many_1_in_a_binary(num):

    counter = 0
    while num:
        if num & 1:
            counter += 1
        num >>= 1
    return counter


if __name__ == '__main__':

    binary_number = '10010000'
    binary_number2 = '01011010'
    integer_number = int(binary_number, 2)
    integer_number2 = int(binary_number2, 2)

    print(f'Integer number: {integer_number}')
    print(f'Binary number: {binary_number}')
    print(f'\nUpdate bit: {update_bit(integer_number, 2, 1)}') 
    print(f'Set bit: {set_bit(integer_number, 2)}')
    print(f'Clear bit: {clear_bit(integer_number, 4)}')
    print(f'\nI: {integer_number}, I2: {integer_number2}')
    print(f'B: {binary_number}, B2: {binary_number2}')
    print(f'Count bits swapped: {count_bits_swapped(integer_number, integer_number2)}')
    print(f'\nSwap bit in place: {swap_bit_in_place(integer_number, integer_number2)}')
    print(f'Find how many 1 in a binary: {find_how_many_1_in_a_binary(integer_number)}')
    