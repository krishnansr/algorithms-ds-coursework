import time
import random, math, sys
from itertools import chain, groupby
from collections import deque
from copy import deepcopy

# sys.setrecursionlimit(10**6)
print('The sys recursion limit is...', sys.getrecursionlimit())


def graph_to_vert_list(graph_edges, no_vertices):
    out_verts = [ [] for _ in range(no_vertices) ]
    in_verts = [ [] for _ in range(no_vertices) ]

    for tail, head in graph_edges:
        out_verts[tail-1].append(head)
        in_verts[head-1].append(tail)
    return out_verts, in_verts

def depth_first_traversal_recursive(adj_list, vertex_no):

    global finishing_time # only modified element

    is_explr_vertex[vertex_no-1] = True
    for connected_vert in adj_list[vertex_no-1]:
        if not is_explr_vertex[connected_vert-1]:
            depth_first_traversal(adj_list, connected_vert)

    finishing_time += 1
    ft_order[vertex_no-1] = finishing_time


def depth_first_traversal(adj_list, vertex_no):

    global finishing_time # only modified element

    dfs_stack.append(vertex_no)
    is_explr_vertex[vertex_no-1] = True

    while len(dfs_stack):

        for connected_vert in adj_list[dfs_stack[-1]-1]:
            if not is_explr_vertex[connected_vert-1]:
                is_explr_vertex[connected_vert-1] = True
                dfs_stack.append(connected_vert)
                break
        else:
            # loop was not broken -> no adjacent unexplored nodes,
            # we're at the end of current dfs branch
            finishing_time += 1
            current_vertex = dfs_stack.pop()
            ft_order[current_vertex-1] = finishing_time
            is_explr_vertex[current_vertex-1] = True


if __name__ == '__main__':
    file_name = 'SCC.txt'
    no_vertices = 875714
    # file_name = 'SCC_test.txt'
    # no_vertices = 9
    # file_name = 'SCC_test1.txt'
    # no_vertices = 12

    with open(file_name) as f:
        graph_edges = [list(map(int, v.split())) for v in f.readlines()]
    out_verts, in_verts = graph_to_vert_list(graph_edges, no_vertices)

    s2 = time.time()
    print('chkpt 1: formed graph, starting first dfs')
    # initialization before first dfs
    finishing_time = 0
    is_explr_vertex = [False]*no_vertices
    ft_order = [-1]*no_vertices
    dfs_stack = deque()
    new_out_verts = [ [] for _ in range(no_vertices)]

    for vertex_no in range(no_vertices, 0, -1):
        if not is_explr_vertex[vertex_no-1]:
            depth_first_traversal(in_verts, vertex_no)

    print('chkpt 2: finished first dfs')
    for ind in range(no_vertices):
        new_out_verts[ft_order[ind]-1] = list(map(lambda x: ft_order[x-1], out_verts[ind]))

    #--------------------------------------------------
    print('chkpt 3: starting second dfs')
    # initialization before second dfs
    is_explr_vertex = [False]*no_vertices
    dfs_stack.clear()
    finishing_time = 0
    scc_size_leader_list = list()

    for vertex_no in range(no_vertices, 0, -1):
        if not is_explr_vertex[vertex_no-1]:
            initial_ft = finishing_time
            depth_first_traversal(new_out_verts, vertex_no)
            scc_size_leader_list.append([finishing_time - initial_ft, vertex_no])
    print('chkpt 4: finished second dfs')

    e2 = time.time()
    print('\n\nfinal SCCs sorted by size...')
    scc_size_leader_list.sort(key=lambda x:x[0], reverse=True)
    scc_size_leader_list.extend([[0, 0]]*5)
    top_five_SCC = [ x[0] for x in scc_size_leader_list[:5] ]
    print(*top_five_SCC, sep=',')

    time2 = e2-s2
    print('graph SCC computation time.......', round(time2, 4))