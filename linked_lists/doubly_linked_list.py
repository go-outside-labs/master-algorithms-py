#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


class Node:

    def __init__(self, data, previous=None):
        self.data = data
        self.next = None
        self.previous = previous

        self.address = self
    
    def insert(self, data):

        while self.next:
            self = self.next
            node = Node(data, previous=self)
        
        if self.next is None:
            node = Node(data, previous=self)
    
        self.next = node
    


if __name__ == "__main__":

    ll = Node(0)
    for n in range(1, 10):
        ll.insert(n)

    while ll.next:
        
        this_data = ll.data
        this_address = ll.address

        if ll.next is None:
            this_next_data = None
            this_next_address = None
        else:
            this_next_data = ll.next.data
            this_next_address = ll.next.address

        if ll.previous is None: 
            this_previous_data = None
            this_previous_address = None
        else:
            this_previous_data = ll.previous.data
            this_previous_address = ll.previous.address


        print(f'This node -> data: {this_data}, address: {this_address} | Previous node -> data: {this_previous_data}, address: {this_previous_address} | Next node -> data: {this_next_data}, address: {this_next_address}')
        ll = ll.next
