#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVLTree():
  
    def __init__(self):
        self.root = None
        self.size = 0
				
    def height(self, node):
        if node:
            return node.height
        return 0
		
    def set_height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))
		
    def right_rotate(self, node):
        new_root = node.left
        node.left = node.left.right
        new_root.right = node
        node.height = self.set_height(node)
        new_root.height = self.set_height(new_root)
        return new_root
    
    def left_rotate(self, node):
        new_root = node.right
        node.right = node.right.left
        new_root.left = node
        node.height = self.set_height(node)
        new_root.height = self.set_height(new_root)
        return new_root
        
    def insert(self, node, val):
        if node == self.root:
            self.size += 1
        if node is None:
            return Node(val)
        if node.val < val:
            node.right = self.insert(node.right, val)
        else:
            node.left = self.insert(node.left, val)
        balance = self.height(node.left) - self.height(node.right)
        if balance > 1:
            if self.height(node.left.left) > self.height(node.left.right):
                node = self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                node = self.right_rotate(node)
        elif balance < -1:
            if self.height(node.right.right) > self.height(node.right.left):
                node = self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                node = self.left_rotate(node)
        else:
            node.height = self.set_height(node)
        return node
    
    def get_min_val(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min_val(node.left)
    
    def remove(self, node, val):
        if node is None:
            return node
        if node.val < val:
            node.right = self.remove(node.right, val)
        elif node.val > val:
            node.left = self.remove(node.left, val)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                right_min_val_node = self.get_min_val(node.right)
                node.val = right_min_val_node.val
                node.right = self.remove(node.right, right_min_val_node.val)
        
        node.height = self.set_height(node)
        balance = self.height(node.left) - self.height(node.right)
        if balance > 1:
            if self.height(node.left.left) > self.height(node.left.right):
                node = self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                node = self.right_rotate(node)
        elif balance < -1:
            if self.height(node.right.right) > self.height(node.right.left):
                node = self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                node = self.left_rotate(node)
        else:
            node.height = self.set_height(node)
        return node
    
    def predecessor(self, node, val):
        if node is None:
            return node
        if node.val == val:
            return val
        elif node.val > val:
            return self.predecessor(node.left, val)
        else:
            right_res = self.predecessor(node.right, val)
            return right_res if right_res else node.val    
            
    def successor(self, node, val):
        if node is None:
            return node
        if node.val == val:
            return val
        elif node.val < val:
            return self.successor(node.right, val)
        else:
            left_res = self.successor(node.left, val)
            return left_res if left_res else node.val


def contains_duplicate_near(self, nums, k, t):

        avltree = AVLTree()
        root = avltree.root

  
        for i, num in enumerate(nums):            
            predecessor = avltree.predecessor(root, num)
            if predecessor is not None and abs(predecessor - num) <= t:
                return True
            successor = avltree.successor(root, num)
            if successor is not None and abs(successor - num) <= t:
                return True
                        
            root = avltree.insert(root, num)
            
            if avltree.size > k:
                root = avltree.remove(root, nums[i-k])
                
        return False
  
