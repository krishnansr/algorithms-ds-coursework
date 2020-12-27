import time
import numpy as np
import math, sys
from pprint import pprint
import heapq

# sys.setrecursionlimit(10**6)
print('The sys recursion limit is...', sys.getrecursionlimit())

def dijkstra_short_paths(adj_list, num_vertices, source_vertex=1, max_dist=1000000):
    # build shortest path heap
    shortest_paths= [max_dist]*num_vertices
    shortest_paths[source_vertex-1] = 0

    dijkstra_heap = list(zip(shortest_paths, range(1, num_vertices+1)))
    heapq.heapify(dijkstra_heap)

    while dijkstra_heap:
        curr_dijkstra_score, curr_vertex_no = heapq.heappop(dijkstra_heap)
        shortest_paths[curr_vertex_no-1] = curr_dijkstra_score
        for connected_edge, length in adj_list[curr_vertex_no-1]:
            if shortest_paths[connected_edge-1] == max_dist:
                # dijkstra greedy score is max_dist -> edge still in V-X bag
                for ind, (djk_score, vert) in enumerate(dijkstra_heap):
                    if vert == connected_edge:
                        break
                old_dist, _ = dijkstra_heap.pop(ind)    # not heap pop so have to heapify
                new_dist = min(curr_dijkstra_score + length, old_dist)
                dijkstra_heap.append((new_dist, connected_edge))

        heapq.heapify(dijkstra_heap)

    return shortest_paths


if __name__ == '__main__':
    # file_name = 'dijkstraTest.txt'
    # req_vertices = [1, 2, 7]
    file_name = 'dijkstraData.txt'
    req_vertices = [7,37,59,82,99,115,133,165,188,197]

    with open(file_name) as f:
        adj_list = [v.split()[1:] for v in f.readlines()]

    num_vertices = len(adj_list)
    graph = list()
    for vertex in range(num_vertices):
        adj_list[vertex] = list(map(lambda x:tuple(map(int, x.split(','))), adj_list[vertex]))

    # pprint(adj_list)
    print('chkpt 1: formed graph, starting dijsktra search')
    shortest_paths = dijkstra_short_paths(adj_list, num_vertices, source_vertex=1, max_dist=1000000)

    print('chkpt 2: finished dijsktra search')
    print(shortest_paths)

    print('chkpt 3: Required vertices lengths...')
    req_vertices_length = [ shortest_paths[i-1] for i in req_vertices ]
    print(','.join(map(str, req_vertices_length)))
    # 2599,2610,2947,2052,2367,2399,2029,2442,2505,3068