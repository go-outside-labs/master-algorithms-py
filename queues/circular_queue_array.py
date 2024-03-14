#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


class CircularQueue:

    def __init__(self, size):
        self.head = 0
        self.tail = 0
        self.size = size
        self.queue = [None] * self.size
        
    def enqueue(self, value: int) -> bool:
            
        if self.is_full():
            return False

        if self.is_empty():
            self.head = 0
        
        while self.queue[self.tail] is not None:
            self.tail += 1 
            if self.tail == self.size:
                self.tail = 0
    
        self.queue[self.tail] = value
        
        return True

    def dequeue(self) -> bool:

        if self.is_empty():
            return False

        value = self.queue[self.head]
        self.queue[self.head] = None
        self.head += 1

        if self.head == self.size:
            self.head = 0

        return True

    def front(self) -> int:
        return self.queue[self.head] or False
        
    def rear(self) -> int:
        return self.queue[self.tail] or False
        
    def is_empty(self) -> bool:
        for n in self.queue:
            if n is not None:
                return False
        return True

    def is_full(self) -> bool:
        for n in self.queue:
            if n is None:
                return False
        return True
        
