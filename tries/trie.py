#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['$'] = None
        
    def match(self, seq, prefix=False) -> bool:
        node = self.root
        for c in seq:
            if c not in node:
                return False
            node = node[c]
        return prefix or ('$' in node)
        
    def search(self, word: str) -> bool:
        return self.match(word)
        
    def starts_with(self, prefix: str) -> bool:
        return self.match(prefix, True)
