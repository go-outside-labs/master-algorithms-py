#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


 
def count_unival(root) -> int:
        
        global count = 0
        
        def dfs(node):
            if node is None:
                return True
            
            if dfs(node.left) and dfs(node.right):
                if (node.left and node.left.val != node.val) or \
                    (node.right and node.right.val != node.val):
                         return False
                self.count += 1
                return True
            
            return False

        dfs(root)
        return count
