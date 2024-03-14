#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def get_row(self, row: int) -> list[int]:
        
        if row == 0: 
            return [1]
	
        result = self.get_row(row - 1)
        
        return [1] + [sum(_) for _ in zip(result, result[1:])] + [1]
