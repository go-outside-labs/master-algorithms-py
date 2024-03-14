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
    def __init__(self, value=None):
        self.val = value
        self.left = None
        self.right = None


class Bucket:
    def __init__(self):
        self.tree = BSTree()

    def insert(self, value):
        self.tree.root = self.tree.insert(self.tree.root, value)
        
    def delete(self, value):
        self.tree.root = self.tree.delete(self.tree.root, value)
    
    def exists(self, value):
        return (self.tree.search(self.tree.root, value) is not None)


class BSTree():
    def __init__(self):
        self.root = None

    def search(self, root, value) -> Node:
        if root is None or value == root.val:
            return root

        return self.search(root.left, value) if val < root.value \
            else self.search(root.right, value)
    
    def insert(self, root, value) -> Node:
        if not root:
            return Node(value)
        
        if value > root.val:
            root.right = self.insert(root.right, value)
        elif value == root.val:
            return root
        else:
            root.left = self.insert(root.left, value)
    
    def successor(self, root):
        # one step right and then all left
        root = root.right
        while root.left:
            root = root.left
        return root.value
    
    def predecessor(self, root):
        # one step left and then always right
        root = root.left
        while root.right:
            root = root.right
        return root.value

    def delete(self, root, key) -> Node:
        if not root:
            return None

        if key > root.val:
            root.right = self.delete(root.right, key)
        
        elif key < root.val:
            root.left = self.delete(root.left, key)
        
        else:
            if not (root.left or root.right):
                root = None
            elif root.right:
                root.val = self.sucessor(root)
                root.right = self.delete(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.delete(root.left, root.val)
        
        return root
    
