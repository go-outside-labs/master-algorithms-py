#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

class Node:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        """Prints the node"""
        return f'{self.value}'


class LinkedListFIFO:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def add_first(self, value):
        self.length = 1
        node = Node(value)
        self.head = node
        self.tail = node
    
    def delete_first(self):
        self.length = 0
        self.head = None
        self.tail = None
  
    def add(self, value):
        self.length += 1
        node = Node(value)
        if self.tail:
            self.tail.right = node
        self.tail = node
    
    def _delete(self, node):
        if not self.head or not self.head.pointer:
            self.delete_first()
        else:
            node, prev, i = self._find(index)
            if i == index and node:
                self.length -= 1
                if i == 0 or not prev:
                    self.head = node.pointer
                else:
                    prev.pointer = node.pointer
                if not self.tail == node:
                    self.tail = prev
    
    def find(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.right
            i += 1
        return node, prev, i


if __name__ == '__main__':

    print('Linked List FIFO')
    ll = LinkedListFIFO()
    print(f'Add 1: {ll.add(1)}')
    print(f'Add 2: {ll.add(2)}')
    print(f'Add 3: {ll.add(3)}')

    print(f'Length: {ll.length}')
    print(f'Find 1: {ll.find(1)}')

    print(f'Delete 1: {ll._delete(1)}')
    print(f'Length: {ll.length}')
    print(f'Find 1: {ll.find(1)}')
