#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein


def num_island_dfs(grid) -> int:
        
        LAND = '1'
        answer = 0

        def dfs(row, col):
          
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != LAND:
                return
            
            grid[row][col] = 'x'
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == LAND:
                    answer += 1
                    dfs(i, j)
  
        return answer


def num_island_bfs(grid) -> int:
        
        LAND = '1'
        answer = 0
        queue = collections.deque()

        def bfs(row, col, queue):
            
            delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            
            while queue:
                x, y = queue.popleft()
                
                for dx, dy in delta:
                    
                    px, py = x + dx, y + dy
                    if px < 0 or px >= len(grid) or py < 0 or py >= len(grid[0]) or grid[px][py] != LAND:
                        continue
                        
                    grid[px][py] = 'x'
                    queue.append((px, py))


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == LAND:
                    answer += 1
                    queue.append((i, j))
                    bfs(i, j, queue)

  
        return answer
