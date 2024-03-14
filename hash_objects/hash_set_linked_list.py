#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


class HashSet:

    def __init__(self, size):
        self.size = size
        self.bucket = [Bucket() for _ in range(self.size)]

    def _get_hash_key(self, key):
        return key % self.size

    def add(self, element: int) -> None:
        bucket_index = self._get_hash_key(element)
        self.bucket[bucket_index].insert(element)
    
    def remove(self, element: int) -> None:
        bucket_index = self._get_hash_key(element)
        self.bucket[bucket_index].delete(element)

    def contains(self, element: int) -> bool:
        bucket_index = self._get_hash_key(element)
        return self.bucket[bucket_index].exists(element)
        

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Bucket:
    def __init__(self):
        self.head = Node(0)

    def insert(self, value):
        if not self.exists(value):
            self.head.next =  Node(value, self.head.next)
        else:
            print(f'node {value} already exists')
        
    def delete(self, value):
        prev = self.head
        current = self.head.next
        while current is not None:
            if current.value == value:
                prev.next = current.next
                return True
            prev = current
            current = current.next
        return False
    
    def exists(self, value):
        current = self.head.next
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False
    
