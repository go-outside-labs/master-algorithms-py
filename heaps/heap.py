#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

class Heap:

    def __init__(self):

        self.heap = []

    def heapify(self, n, i):

        largest = i
        left_children = 2 * i + 1
        right_children = 2 * i + 2

        if left_children < n and self.heap[i] < self.heap[left_children]:
            largest = left_children

        if right_children < n and self.heap[largest] < self.heap[right_children]:
            largest = right_children

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(n, largest)


    def insert(self, num):

        size = len(self.heap)

        if size == 0:
            self.heap.append(num)

        else:
            self.heap.append(num)
            for i in range((size // 2) - 1, -1, -1):
                self.heapify(size, i)


    def delete_node(self, num):

        size = len(self.heap)

        i = 0
        for i in range(size):
            if num == self.heap[i]:
                break

        self.heap[i], self.heap[size - 1] = self.heap[size - 1], self.heap[i]

        self.heap.remove(size - 1)

        for i in range((len(self.heap) // 2) - 1, -1, -1):
            self.heapify(len(self.heap), i)



if __name__ == '__main__':

    h = Heap()
    for n in [10, 4, 9, 8, 1, 2]:
        h.insert(n)

    print (f'Max-heap array: {h.heap}')

    n = 2
    h.delete_node(n)
    print(f'After deleting {n}: {h.heap}')
