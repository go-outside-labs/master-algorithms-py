#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def heap_sort(self, array) -> list:

      def max_heapify(heap_size, index):
        
            left, right = 2 * index + 1, 2 * index + 2
            largest = index
        
            if left < heap_size and array[left] > array[largest]:
                largest = left
            elif if right < heap_size and array[right] > array[largest]:
                largest = right
            elif largest != index:
                array[index], array[largest] = array[largest], array[index]
                max_heapify(heap_size, largest)

      for i in range(len(lst) // 2 - 1, -1, -1):
            max_heapify(len(array), i)

      for i in range(len(array) - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            max_heapify(i, 0)
        
      return array
