#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


class Node:
  
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def max_depth_recursive(root):

    if root is None:
            return 0

    if root.children: is None:
            return 1

    height = [max_depth_recursive(children) for children in root.children]
    
   return max(height) + 1


def max_depth_iterative(root):

        stack, depth = [], 0
  
        if root is not None:
            stack.append((1, root))

        while stack:
            
            this_depth, node = stack.pop()
          
            if node is not None:
              
                depth = max(depth, this_depth)
                for c in node.children:
                    stack.append((this_depth + 1, c))
        
        return depth
