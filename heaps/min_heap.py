#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

class MinHeap:

    def __init__(self, size):

        self.heapsize = size
        self.minheap = [0] * (size + 1)
        self.realsize = 0

    def add(self, element):

        if self.realsize + 1 > self.heapsize:
            print("Too many elements!")
            return False

        self.realsize += 1
        self.minheap[self.realsize] = element

        index = self.realsize
        parent = index // 2

        while self.minheap[index] < self.minheap[parent] and index > 1:

            self.minheap[parent], self.minheap[index] = self.minheap[index], self.minheap[parent]
            index = parent
            parent = index // 2
    
    def peek(self):

        return self.minheap[1]
    
    def pop(self):

        if self.realsize < 1:
            print("Heap is empty.")
            return False

        else:
            remove_element = self.minheap[1]
            self.minheap[1] = self.minheap[self.realsize]
            self.realsize -= 1
            index = 1

            while index <= self.realsize // 2:

                left_children = index * 2
                right_children = (index * 2) + 1

                if self.minheap[index] > self.minheap[left_children] or \
                   self.minheap[index] > self.minheap[right_children]:

                    if self.minheap[left_children] < self.minheap[right_children]:

                        self.minheap[left_children], self.minheap[index] = self.minheap[index], self.minheap[left_children]
                        index = left_children
                    
                    else:

                        self.minheap[right_children], self.minheap[index] = self.minheap[index], self.minheap[right_children]
                        index = right_children
                else:
                    break

            return remove_element
    
    def size(self):
        return self.realsize
    
    def __str__(self):
        return str(self.minheap[1 : self.realsize + 1])
        

if __name__ == "__main__":
    	# Test cases
        h = MinHeap(5)
        h.add(3)
        h.add(1)
        h.add(2)

        print(h)
        print(h.peek())
        print(h.pop())
        print(h.pop())
        print(h.pop())
        h.add(4)
        h.add(5)
        print(h)
