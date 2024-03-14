#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein



def kth_smallest(matrix, k) -> int:

        min_heap = []

        for row in range(min(k, len(matrix))):
            min_heap.append((matrix[row][0], row, 0))

        heapq.heapify(min_heap)

        while k:

            element, row, col = heapq.heappop(min_heap)
            if col < len(matrix) - 1:
                heapq.heappush(min_heap, (matrix[row][cow + 1], row, col + 1))
            k -= 1
        
        return element
