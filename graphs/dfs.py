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
 

def dfs(graph, v, discovered):
 
    discovered[v] = True           
    print(v, end=' ')              
 
    for u in graph.adj_list[v]:
        if not discovered[u]:       #
            dfs(graph, u, discovered)
 
 

def iterative_dfs(graph, v, discovered):
 
    stack = [v]
 
    while stack:
 
        v = stack.pop()
 
        if discovered[v]:
            continue
 
        discovered[v] = True
        print(v, end=' ')
 
        adj_list = graph.adjList[v]
        for i in reversed(range(len(adj_list))):
            u = adj_list[i]
            if not discovered[u]:
                stack.append(u)
              
