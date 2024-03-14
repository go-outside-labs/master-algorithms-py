#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def matrix_bfs(rooms) -> None:
        
        m = len(rooms)
        if m == 0:
           return rooms
        n = len(rooms[0])
        
        GATE = 0
        EMPTY = 2147483647
        DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))

        queue = collections.deque()

        for i in range(m):
            for j in range(n):
                
                if rooms[i][j] == GATE:
                    q.append((i, j))

        while queue:

            row, col = queue.popleft()

            for (x, y) in DIRECTIONS:

                r = row + x
                c = col + y

                if (r < 0) or (c < 0) or (r >= m) or (c >= n) or rooms[r][c] != EMPTY:
                    continue

                rooms[r][c] = rooms[row][col] + 1
                queue.append((r, c))            
