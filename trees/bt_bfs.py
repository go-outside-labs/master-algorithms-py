#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def bfs(root) -> list:

        result = []
        queue = collections.deque([root])
        
        while queue:
    
            node = queue.popleft()
                
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        
        return result
