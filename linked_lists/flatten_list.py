#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein



class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def dfs(prev, node):
  
        if not node:
            return prev

        node.prev = prev
        prev.next = node
        temp_next = node.next
  
        last = dfs(node, node.child)
        node.child = None
  
        return dfs(last, temp_next)


def flatten(head):
        
        if head is None:
            return head

        sentinel = Node(None, None, head, None)
    
        dfs(prev=sentinel, node=head)

        # erase the pointer to sentinel and return
        sentinel.next.prev = None 
        return sentinel.next
