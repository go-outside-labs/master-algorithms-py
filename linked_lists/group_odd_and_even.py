#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

class Node:

   def __init__(self, val):
       self.val = val
       self.next = None


def group_odd_and_even(head):
        
        if not head:
            return None
        
        odd = head
        even = odd.next
        even_head = even
        
        while even is not None and even.next is not None:
            
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = even_head
        
        return head
        
