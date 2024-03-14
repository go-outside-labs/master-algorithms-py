#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def rotate_list_by_k(head, k):
        
    if head is None:
        return head

    # get the size of the list
    end, n = head, 1
    while end.next:
        end = end.next
        n += 1

    # rotate
    end.next = head
    new_end, i = head, 0
    while i < n - (k % n) - 1:     
        new_end = new_end.next
        i += 1

    # remove cycle
    new_head = new_end.next
        
    return new_head
