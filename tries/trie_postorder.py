#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def postorder(self, root: 'Node'):
        
    if root is None:
        return []

    stack, result = [root, ], []

    while stack:
            
      node = stack.pop()
            
      if node is not None:
          result.append(node.val)
              
      for c in node.children:
          stack.append(c)
        
    return result[::-1]
  
