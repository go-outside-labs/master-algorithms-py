#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

def preorder(root) -> list:
        
  if root is None:
      return []
    
  return [root.val] + preorder(root.left) + preorder(root.right)
    
        
def preorder_iterative(root) -> list:
        
        result = []
        stack = [root]
        
        while stack:
            
            node = stack.pop()
            
            if node:
                result.append(node.val) 
                stack.append(node.right) # not the order 
                stack.append(node.left)
            
        return result
