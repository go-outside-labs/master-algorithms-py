#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def height(root):
  
    if root is None:
      return -1
      
    return 1 + max(height(root.left), height(root.right))


def is_balanced(root):
  
    if root is None:
      return True

    return abs(height(root.left) - height(root.right)) < 2 and \
            is_balanced(root.left) and is_balanced(root.right)
        
