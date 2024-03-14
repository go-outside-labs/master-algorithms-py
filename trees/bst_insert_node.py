#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def bst_insert_iterative(root, val):

  node = root
  while node:
    
    if val > node.val:
        if not node.right:
          node.right = Node(val)
          break
        else:
          node = node.right
    
    else:
        if not node.left:
          node.left = Node(val)
          break
        else:
          node = node.left
        
  return root


def bst_insert_recursive(root, val):
        
    if root is None:
        return Node(val)

    if val > root.val:
        root.right = self.bst_insert_recursive(root.right, val)
        
    else:
        root.left = self.bst_insert_recursive(root.left, val)
        
    return root
