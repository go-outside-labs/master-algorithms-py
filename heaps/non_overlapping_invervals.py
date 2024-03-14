#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def non_overlapping_invervals(intervals):
        
        if not intervals:
            return 0

        result = []
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(result, intervals[0][-1])

        for interval in intervals[1:]:

            if result[0] <= interval[0]:
                heapq.heappop(result)
            
            heapq.heappush(result, interval[1])
        
        return len(result)
