#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def compare_two_tops(array) -> int:

        for i in range(len(array)):
            array[i] *= -1

        heapq.heapify(array)

        while len(array) > 1:

            val1 = heapq.heappop(array)
            val2 = heapq.heappop(array)

            if val1 != val2:
                heapq.heappush(array, val1 - val2)

        if array:
            return -heapq.heappop(array)
            
        return 0
          
