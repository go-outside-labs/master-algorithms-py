#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

class Node:

   def __init__(self, val):
       self.val = val
       self.next = None


def has_cycle(head) -> bool:
        
        if not head:
            return False
        
        p1 = head
        p2 = head.next
        
        while p1 != p2:
            
            if not p1 or not p2 or not p2.next:
                return False
            
            p1 = p1.next
            p2 = p2.next.next
        
        return True
            
