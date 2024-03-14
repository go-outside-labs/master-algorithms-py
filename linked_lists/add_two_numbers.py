#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


class Node:

   def __init__(self, val):
       self.val = val
       self.next = None


def add_two_numbers(l1, l2):
  
        n1, n2, i = '', '', 1
        
        while l1:
            n1 += str(l1.val)
            l1 = l1.next
            
        while l2:
            n2 += str(l2.val)
            l2 = l2.next
            
        n1 = int(n1[::-1])
        n2 = int(n2[::-1])
        n = str(n1 + n2)[::-1]
    
        current = Node(n[0])
        head = current
     
        while i < len(n):
            current.next = Node(n[i])
            current = current.next
            i += 1
   
        return head
  
