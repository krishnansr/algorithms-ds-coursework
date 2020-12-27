import time
import numpy as np
import math, sys
from pprint import pprint
import heapq

print('The sys recursion limit is...', sys.getrecursionlimit())


def prim_MST(adj_list, num_vertices, source_vertex=1, max_dist=1000000):
    # build shortest path heap
    shortest_paths= [max_dist]*num_vertices
    shortest_paths[source_vertex-1] = 0
    mst_list = np.zeros(num_vertices, dtype=np.int64)
    disc_vertices = [False]*num_vertices

    dijkstra_heap = list(zip(shortest_paths, range(1, num_vertices+1)))
    heapq.heapify(dijkstra_heap)

    while dijkstra_heap:
        curr_dist, curr_vertex_no = heapq.heappop(dijkstra_heap)
        mst_list[curr_vertex_no-1] = curr_dist
        disc_vertices[curr_vertex_no-1] = True

        for connected_vertex_no, connected_length in adj_list[curr_vertex_no-1]:
            if not disc_vertices[connected_vertex_no-1]:
                # dijkstra greedy score is max_dist -> edge still in V-X bag
                for ind, (djk_score, vert) in enumerate(dijkstra_heap):
                    if vert == connected_vertex_no:
                        break
                old_dist, _ = dijkstra_heap.pop(ind)    # not heap pop so have to heapify
                new_dist = min(connected_length, old_dist)
                dijkstra_heap.append((new_dist, connected_vertex_no))

        heapq.heapify(dijkstra_heap)

    return mst_list


if __name__ == '__main__':
    file_name = 'edges.txt'
    # file_name = 'edgesTest.txt'

    with open(file_name, 'r') as f:
        num_vertices, num_edges = list(map(int, f.readline().split()))
        edge_list = [ list(map(int, v.split())) for v in f.readlines()]

    adj_list = [ [] for _ in range(num_vertices) ]
    for edge1, edge2, cost in edge_list:
        adj_list[edge1-1].append([edge2, cost])
        adj_list[edge2-1].append([edge1, cost])

    # pprint(adj_list)
    print('chkpt 1: formed graph, searching MST using prim\'s algorithms...')

    mst_list = prim_MST(adj_list, num_vertices, source_vertex=1, max_dist=1000000)
    print('chkpt 2: finished MST search... MST cost is...', np.sum(mst_list))   #-3612829
