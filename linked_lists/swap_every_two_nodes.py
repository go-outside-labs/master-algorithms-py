#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


class Node:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next


def swap_pairs(head: Optional[Node]) -> Optional[Node]:
  
      if not head or not head.next:
          return head

      first_node = head
      second_node = head.next

      first_node.next = swap_pairs(second_node.next)
      second_node.next = first_node

      return second_node
