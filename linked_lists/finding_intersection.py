#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

class Node:
    def __init__(self, val):
      self.val = val
      self.next = None


def get_intersection_node(self, head_a: Node, head_b: Node) -> Optional[Node]:
        
        seen_b = set()
        
        while head_b is not None:
            
            seen_b.add(head_b)
            head_b = head_b.next

        while head_a is not None:

            if head_a in seen_b:
                return head_a
            
            head_a = head_a.next
        
