#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

'''
Given a stream of integers and a window size, calculate the moving average in the sliding window.
'''

class MovingAverage:

    def __init__(self, size: int):
        
        self.queue = []
        self.size = size
        

    def next(self, val: int) -> float:
        
        self.queue.append(val)
        
        if len(self.queue) > self.size:
            self.queue.pop(0)
        
        return sum(self.queue) / len(self.queue)
    
