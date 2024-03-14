#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def delete_node_without_head(node):

  node.val = node.next.val
  node.next = node.next.next
  
