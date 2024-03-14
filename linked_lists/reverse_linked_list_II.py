#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


class Node:
    def __init__(self, val=0, next):
        self.val = val
        self.next = next


def reverse_list(head: Optional[Node]) -> Optional[Node]:

   if head is None:
       return head

   prev = None
   curr = head
        
   while curr:
       next_temp = curr.next     
       curr.next = prev          
       prev = curr               
       curr = next_temp          

   return prev
    
