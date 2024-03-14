#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def preorder(root: 'Node'):
        
        if root is None:
            return []
        
        stack, result = [root, ], []

        while stack:
                
            node = stack.pop()
            result.append(node.val)
            stack.extend(node.children[::-1])
            
        return result
