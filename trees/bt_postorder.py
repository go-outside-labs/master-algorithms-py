#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

def postorder(root) -> list:
        
    if root is None:
      return []
    
    return postorder(root.left) + postorder(root.right) + [root.val] 
        

def postorder_iterative(root) -> list:
        
    stack, result = [], []
    node = root
    
    while node or stack:

            while node:
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            
            if stack and node.right == stack[-1]:
                stack[-1] = node
                node = node.right

            else:
                result.append(node.val)
                node = None
                
    return result
        
