#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def top_k_frequent_values(list, k):
        
        if k == len(nums):
                return nums

        # hashmap element: frequency
        counter = Counter(nums)
        return heapq.nlargest(k, counter.keys(), key=counter.get)
