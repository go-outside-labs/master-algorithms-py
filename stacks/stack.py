#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


class Stack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        self.stack.append((val, self.min))
        if self.min is not None:
            self.min = min(self.min, val)
        else:
            self.min = val

    def pop(self) -> None:
        if self.stack:
            (val, prior_min) = self.stack.pop()
            self.min = prior_min
            return val
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def get_min(self) -> int:
        return self.min
        
