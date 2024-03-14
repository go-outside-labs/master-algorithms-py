#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


class Node:
   def __init__(self, x):
       self.val = x
       self.next = None


def detect_cycle(head):

        seen = set()
        node = head

        while node is not None:

            if node in seen:
                return node

            else:
                seen.add(node)
                node = node.next

        return None
  
