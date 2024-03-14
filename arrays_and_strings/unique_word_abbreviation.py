#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

'''
The abbreviation of a word is a concatenation of its first letter, 
the number of characters between the first and last letter, and its 
last letter. If a word has only two characters, then it is an abbreviation of itself.
Returns true if either of the following conditions are met (otherwise returns false):
- There is no word in dictionary whose abbreviation is equal to word's abbreviation.
- For any word in dictionary whose abbreviation is equal to word's abbreviation, 
that word and word are the same.
'''

class ValidWordAbbr:

    def __init__(self, dictionary):
        
        self.dict = collections.defaultdict(set)
        for w in dictionary:
            aux_dict[self.get_abr(w)].add(w)
            
        return aux_dict
        
    def get_abr(self, word):
        
        return word[0] + str(len(word[1:-1])) + word[-1] if len(word) != 2 else word
        
    def is_unique(self, word: str) -> bool:
        
        abr = self.get_abr(word)
        words = self.dict[abr]
        
        return len(words) == 0 or (len(words) == 1 and word in words)
    
