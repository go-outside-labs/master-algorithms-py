#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def is_valid_bst_iterative(root):
        
        queue = deque((root, float(-inf), float(inf)))
        
        while queue:
          
            node, min_val, max_val = queue.popleft()
          
            if node:
                if min_val >= node.val or node.val >= max_val:
                    return False
                queue.append((node.left, min_val, node.val))
                queue.append((node.right, node.val, max_val))
        
        return True


def is_valid_bst_recursive(root, min_val=float(-inf), max_val=float(inf)):
            
        if root is None:
            return True
        
        return (min_val < root.val < max_val) and \
                  is_valid_bst_recursive(root.left, min_val, root.val) and \
                  is_valid_bst_recursive(root.right, root.val, max_val)
    
    
def is_valid_bst_inorder(root):
        
        def inorder(node):
            if node is None:
                return True
            
            inorder(node.left)
            stack.append(node.val)
            inorder(node.right)
            
        stack = []
        inorder(root)
  
        for i in range(1, len(stack)):
            if queue[i] <= queue[i - 1]:
                return False
            
        return True
