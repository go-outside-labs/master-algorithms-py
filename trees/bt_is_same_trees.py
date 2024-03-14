#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def is_same_trees(p, q):

        if not p and not q:
            return True
        
        if (not p and q) or (not q and p) or p.val != q.val:
            return False
        
        return is_same_trees(p.right, q.right) and is_same_trees(p.left, q.left)
