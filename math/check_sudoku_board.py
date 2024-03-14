#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
'''

def is_valid_sudoku(board) -> bool:
        
  N = 9

  rows = [set() for _ in range(N)]
  cols = [set() for _ in range(N)]
  boxes = [set() for _ in range(N)]
            
  for r in range(N):
    for c in range(N):
      val = board[r][c]
      if val == '.':
        continue
                
      if val in rows[r]:
        return False
      rows[r].add(val)

      if val in cols[c]:
        return False
      cols[c].add(val)

      index = (r // 3) * 3 + c // 3
      if val in boxes[index]:
        return False
      boxes[index].add(val)
        
  return True
        
