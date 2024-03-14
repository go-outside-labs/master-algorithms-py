#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def build_tree(preorder, inorder):
        
        def helper(left, right, index_map):
            
            if left > right:
                return None
                    
            node = preorder.pop(0) # this order change from postorder
            root = Node(node.val) 
            index_here = index_map[node.val]

            root.left = helper(left, index_here - 1, index_map) # this order change from postorder
            root.right = helper(index_here + 1, right, index_map)
            
            return root
        
        index_map = {value: i for i, value in enumerate(inorder)}
        
        return helper(0, len(inorder) - 1, index_map)
        
