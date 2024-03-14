#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def quick_sort_partition(array):

    pivot, array = array[0], array[1:]

    lower = [i for i in array if i <= pivot]
    higher = [i for i in array if i > pivot]

    return lower, pivot, higher


def quick_sort_divided(array):

    if len(array) < 2:
        return array

    lower, pivot, higher = quick_sort_partition(array)
    
    return quick_sort_divided(lower) + [pivot] + quick_sort_divided(higher)

