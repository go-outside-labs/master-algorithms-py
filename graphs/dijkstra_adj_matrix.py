#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

# dijkstra's single source shortest path algorithm
# with adjacency matrix representation

import sys


class Graph():

	def __init__(self, vertices):

		self.V = vertices
		self.graph = [[0 for col in range(vertices)] for row in range(vertices)]

	def print_solution(self, dist):

		print("Vertex \tDistance from Source")
		for node in range(self.V):
			print(node, "\t", dist[node])

	def min_distance(self, dist, sset):

		# minimum distance for next node
		min_ = sys.maxsize

		# search not nearest vertex not in the shortest path tree
		for u in range(self.V):
			if dist[u] < min_ and sset[u] == False:
				min_ = dist[u]
				min_index = u

		return min_index


	def dijkstra(self, src):

		dist = [sys.maxsize] * self.V
		dist[src] = 0
		sset = [False] * self.V

		for c in range(self.V):
			x = self.min_distance(dist, sset)
			sset[x] = True

			for y in range(self.V):
				if self.graph[x][y] > 0 and \
                   sset[y] == False and \
                   dist[y] > dist[x] + self.graph[x][y]:
					    dist[y] = dist[x] + self.graph[x][y]

		self.print_solution(dist)


if __name__ == "__main__":
	g = Graph(9)
	g.graph = [     [0, 4, 0, 0, 0, 0, 0, 8, 0],
			        [4, 0, 8, 0, 0, 0, 0, 11, 0],
			        [0, 8, 0, 7, 0, 4, 0, 0, 2],
			        [0, 0, 7, 0, 9, 14, 0, 0, 0],
			        [0, 0, 0, 9, 0, 10, 0, 0, 0],
			        [0, 0, 4, 14, 10, 0, 2, 0, 0],
			        [0, 0, 0, 0, 0, 2, 0, 1, 6],
			        [8, 11, 0, 0, 0, 0, 1, 0, 7],
			        [0, 0, 2, 0, 0, 0, 6, 7, 0]
			]

	g.dijkstra(0)
