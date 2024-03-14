#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

import random


class RandomizedSet:

    def __init__(self):
        
        self.random_set = {}
        self.index_list = []
        
    def insert(self, val: int) -> bool:
        
        if val in self.random_set.keys():
            return False
            
        self.index_list.append(val)
        self.random_set[val] = len(self.index_list)
        
        return True

    def remove(self, val: int) -> bool:
        
        if val in self.random_set.keys():
            
            last_element = self.index_list[-1]
            index_val = self.random_set[val]
            self.index_list[index_val] = last_element
            self.random_set[last_element] = index_val
            
            self.index_list.pop()
            del self.random_set[val]
            
            return True
            
        return False
        
    def get_random(self) -> int:
        
        return random.choice(self.index_list)
  
