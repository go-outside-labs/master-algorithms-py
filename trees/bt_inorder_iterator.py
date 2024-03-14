#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

class Node:
  def __init__(self, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right


class InorderIterator:

    def __init__(self, root):
        self.stack = []
        self.left_inorder(root)
        
    def left_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        top_node = self.stack.pop()
        if top_node.right:
            self.left_inorder(top_node.right)
        return top_node.val
        
    def has_next(self) -> bool:
        return len(self.stack) > 0
        
