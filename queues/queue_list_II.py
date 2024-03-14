#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

class CircularQueue:

    def __init__(self, size):
        self.head = 0
        self.count = 0
        self.queue = [0] * size
        self.size = size

    def _get_tail(self):
        return (self.head + self.count - 1) % self.size

    def _get_next_tail(self):
        return (self.head + self.count) % self.size

    def _get_next_head(self):
        return (self.head + 1) % self.size

    def enqueue(self, value: int) -> bool:

        if self.is_empty():
          return False
          
        self.queue[self._get_next_tail()] = value
        self.count += 1
      
        return True

    def dequeue(self) -> bool:

        if self.is_empty():
          return False
          
        self.head = self._get_next_head()
        self.count -= 1
      
        return True

    def Front(self) -> int:
        if self.is_empty():
          return False
        
      return self.queue[self.head]

    def Rear(self) -> int:
        if self.is_empty():
          return False
          
        return self.queue[self._get_tail()]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size
