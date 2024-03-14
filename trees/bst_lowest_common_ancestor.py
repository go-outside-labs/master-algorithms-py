#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def lowest_common_ancestor(root, p, q):

        node, result = root, root
        
        while node:
            
            result = node
            
            if node.val > p.val and node.val > q.val:
                node = node.left
                
            elif node.val < p.val and node.val < q.val:
                node = node.right
                
            else:
                break
        
        return result
