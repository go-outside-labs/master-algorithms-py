#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def lowest_common_ancestor(root, p, q):

    stack = [root]
    parent = {root: None}
    
    while p not in parent or q not in parent:

        node = stack.pop()
        if node:
            parent[node.left] = node
            parent[node.right] = node
            stack.append(node.left)
            stack.append(node.right)

    ancestors = set()
    while p:
        ancestors.add(p)
        p = parent[p]

    while q not in ancestors:
        q = parent[q]
            
    return q
                
