#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def build_tree(left, right, index_map, postorder):
            
        if left > right:
                return None

        node = postorder.pop() # this order change from preorder
        root = Node(node.val)  
        index_here = index_map[node.val]

        root.right = build_tree(index_here + 1, right, index_map, postorder) # this order change from preorder
        root.left = build_tree(left, index_here - 1, index_map, postorder)
            
        return root


def build_tree(inorder, postorder):

        index_map = {val: i for i, value in enumerate(inorder)}
            
        return fill_tree(0, len(inorder) - 1, index_map, postorder)
    
