#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

class Node:
    
    def __init__(self, val):
        
        self.val = val
        self.next = None

class LinkedList:

    def __init__(self):
        
        self.head = Node(0)
        self.len = 0
        
    def _loop(self , index):
        
        node = self.head
        p = 0
        while p < index + 1:
            node = node.next
            p += 1
        
        return node
        
    def get(self, index: int) -> int:
        if self.len <= index or index < 0:
            return -1
        
        node = self._loop(index)
        
        return node.val

    def add_at_head(self, val: int) -> None:
        
        self.add_at_index(0, val)


    def add_at_tail(self, val: int) -> None:
        
        self.add_at_index(self.len, val)
        

    def add_at_index(self, index: int, val: int) -> None:
        
        if self.len < index:
            return -1

        if index < 0:
            index = 0
        
        self.len += 1

        node = self.head
        for _ in range(index):
            node = node.next
    
        new_node = Node(val)
        new_node.next = node.next
        node.next = new_node

    def delete_at_index(self, index: int) -> None:
        
        if self.len <= index or index < 0:
            return -1
        
        self.len -= 1

        node = self.head
        for _ in range(index):
            node = node.next
            
        node.next = node.next.next
