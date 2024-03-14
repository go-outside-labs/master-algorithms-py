#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

class MaxHeap:
    def __init__(self, heapsize):

        self.heapsize = heapsize
        self.maxheap = [0] * (heapsize + 1)
        self.realsize = 0

    def add(self, element):

        self.realsize += 1
        if self.realsize > self.heapsize:
            print("Too many elements!")
            self.realsize -= 1
            return False

        self.maxheap[self.realsize] = element
        index = self.realsize
        parent = index // 2

        while self.maxheap[index] > self.maxheap[parent] and index > 1:
            self.maxheap[parent], self.maxheap[index] = self.maxheap[index], self.maxheap[parent]
            index = parent
            parent = index // 2
            
    def peek(self):

        return self.maxheap[1]
    
    def pop(self):

        if self.realsize < 1:
            print("Heap is empty.")
            return False
        else:
            remove_element = self.maxheap[1]
            self.maxheap[1] = self.maxheap[self.realsize]
            self.realsize -= 1
            index = 1

            while (index <= self.realsize // 2):

                left_children = index * 2
                right_children = (index * 2) + 1

                if (self.maxheap[index] < self.maxheap[left_children] or self.maxheap[index] < self.maxheap[right_children]):
                    if self.maxheap[left_children] > self.maxheap[right_children]:
                        self.maxheap[left_children], self.maxheap[index] = self.maxheap[index], self.maxheap[left_children]
                        index = left_children
                    else:
                        self.maxheap[right_children], self.maxheap[index] = self.maxheap[index], self.maxheap[right_children]
                        index = right_children
                else:
                    break
            return remove_element
    
    def size(self):
        return self.realsize
    
    def __str__(self):
        return str(self.maxheap[1 : self.realsize + 1])
        

if __name__ == "__main__":

        h = MaxHeap(5)
        h.add(1)
        h.add(2)
        h.add(3)
        print(h)

        print(h.peek())
        print(h.pop())
        print(h.pop())
        print(h.pop())
        h.add(4)
        h.add(5)
        print(h)
        
