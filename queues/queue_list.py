#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


class Node:
    def __init__(self, value, next=None):
        
        self.value = value
        self.next = next


class Queue:

    def __init__(self, size):
        
        self.size = size
        self.count = 0
        self.head = None
        self.tail = None
        
    def enqueue(self, value: int) -> bool:
        
        if self.is_full():
            return False
            
        if self.is_empty():
            self.head = self.tail = Node(value)
        
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        
        self.count += 1
        
        return True

    def dequeue(self) -> bool:
        
        if self.is_empty():
            return False
             
        self.head = self.head.next
        self.count -= 1
        
        return True

    def front(self) -> int:
        if self.is_empty():
            return False
        return self.head.value

    def rear(self) -> int:
        if self.is_empty():
            return False
        return self.tail.value
    
    def is_empty(self) -> bool:
        return self.count == 0

    def is_full(self) -> bool:
        return self.count == self.size
      
