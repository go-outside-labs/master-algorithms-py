#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def search_bst_recursive(root, val):
        
        if root is None or root.val == val:
            return root
        
        if val > root.val:
            return search_bst_recursive(root.right, val)
        
        else:
            return search_bst_recursive(root.left, val) 


        
def search_bst_iterative(root, val):
        
        while root:
            
            if root.val == val:
                break

            if root.val < val:
                root = root.right

            else:
                root = root.left
        
        return root
