#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

from collections import deque
 

class Graph:

    def __init__(self, edges, n):
 
        self.adj_list = [[] for _ in range(n)]
      
        for (src, dest) in edges:
            self.adj_list[src].append(dest)
            self.adj_list[dest].append(src)
 
 
def bfs(graph, v, discovered):
 
    queue = deque(v)
    discovered[v] = True
 
    while queue:
 
        v = queue.popleft()
        print(v, end=' ')
 
        for u in graph.adj_list[v]:
            if not discovered[u]:
                discovered[u] = True
                queue.append(u)


def recursive_bfs(graph, queue, discovered):
 
    if not queue:
        return
 
    v = queue.popleft()
    print(v, end=' ')
 
    for u in graph.adj_list[v]:
        if not discovered[u]:
            discovered[u] = True
            queue.append(u)
 
    recursive_bfs(graph, queue, discovered)
  
