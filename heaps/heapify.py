#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


import heapq

min_heap = [3,1,2]
heapq.heapify(min_heap)

max_heap = [-x for x in min_heap]
heapq.heapify(max_heap)

heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, -5)

min_elem = min_heap[0]
max_elem = -1 * max_heap[0

heapq.heappop(min_heap)
heapq.heappop(max_heap)

size_min_heap = len(min_heap)
size_max_heap = len(max_heap)
