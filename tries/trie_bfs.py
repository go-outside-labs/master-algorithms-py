#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def level_orders(root):

    if root is None:
        return []

    result = []
    queue = collections.deque([root])

    while queue:
        level = []
        
        for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                queue.extend(node.children)
            result.append(level)
        
  return result
