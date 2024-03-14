#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def is_symmetric(root) -> bool:
        
        stack = [(root, root)]
        
        while stack:
            
            node1, node2 = stack.pop()
            
            if (not node1 and node2) or (not node2 and node1):
                return False
            
            elif node1 and node2 and node1.val != node2.val:
                 return False

            elif not node1 and not node2:
                continue
            
            stack.append([node1.left, node2.right])
            stack.append([node1.right, node2.left])
        
        return True


def is_symmetric_recursive(root) -> bool:
            
        def helper(node1, node2):
                if (not node1 and node2) or \
                   (not node2 and node1) or \
                   (node1 and node2 and node1.val != node2.val):
                        return False
                
                if (not node1 and not node2):
                        return True
                
                return helper(node1.left, node2.right) and helper(node2.left, node1.right)
            
        return helper(root.left, root.right)
            
