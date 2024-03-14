#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def remove_kth_node(self, head, n):
  
        if head is None or head.next is None:
            return None

        # find the length of the list
        node, length = head, 0
        while node:
            node = node.next
            length += 1

        # if n is the entire list, remove head
        if n == length:
            return head.next
    
        # loop to kth element
        node, i = head, 0
        while i <= length - n:
            node = node.next
            i += 1

        # remove the kth element
        node.next = node.next.next
                
        return head
