#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def is_isomorphic(s: str, t: str) -> bool:
        
        map_s_to_t = {}
        map_t_to_s = {}
        
        for ss, tt in zip(s, t):
            
            if (ss not in map_s_to_t) and (tt not in map_t_to_s):
                map_s_to_t[ss] = tt
                map_t_to_s[tt] = ss
            
            elif (map_s_to_t.get(ss) != tt) or (map_t_to_s.get(tt) != ss):
                return False

        return True
