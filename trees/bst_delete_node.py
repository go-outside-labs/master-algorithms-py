#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def successor(root):
   
    root = root.right
    while root.left:
         root = root.left
    return root.val


def predecessor(root):
  
    root = root.left
    while root.right:
         root = root.right
    return root.val


def delete_node(root, key):
        
    if root is None:
         return root

    if key > root.val:
         root.right = delete_node(root.right, key)
      
    elif key < root.val:
            root.left = delete_node(root.left, key)
      
    else:
        if not (root.left or root.right):
            root = None
          
        elif root.right:
            root.val = successor(root)
            root.right = delete_node(root.right, root.val)
          
        else:
            root.val = predecessor(root)
            root.left = delete_node(root.left, root.val)
        
    return root
        
