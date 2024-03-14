#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def inorder(root) -> list:
        
  if root is None:
      return []
    
  return inorder(root.left) + [root.val] + inorder(root.right)
        

def inorder_iterative(root) -> list:
        
        result = []
        stack = []
        node = root
        
        while stack or node:

            if node:
		stack.append(node)
                node = node.left
            else: 
                node = stack.pop()
                result.append(node.val)
                node = node.right
            
        return result
        
