#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

class Node:
    def __init__(self, val=0, next):
        self.val = val
        self.next = next


def reverse_list(head: Optional[Node]) -> Optional[Node]:
            
        if not head or not head.next:
            return head
                
        new_head = reverse_list(head.next)
        head.next.next = head
        head.next = None
         
        return new_head
