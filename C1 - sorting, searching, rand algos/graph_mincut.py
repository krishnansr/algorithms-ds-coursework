import time
import random, math, sys
from itertools import chain
from copy import deepcopy

print('The sys recursion limit is...', sys.getrecursionlimit())

def graph_min_cut(graph):
    active_vertices = set(chain.from_iterable(graph))
    if len(active_vertices) <= 2:
        return len(graph)
    else:
        # contract a random edge
        del_edge = random.choice(graph)
        self_loops = list()
        for ind, edge in enumerate(graph):
            if del_edge[1] in edge:
                if del_edge[0] in edge:
                    self_loops.append(ind)
                else:
                    graph[ind].remove(del_edge[1])
                    graph[ind].append(del_edge[0])
                    graph[ind].sort()

        # remove self loops
        # print('graph before deleting...', graph)
        for i in self_loops[::-1]:
            graph.pop(i)
        # print('deleted edge and graph after deleting...', del_edge, graph)
        return graph_min_cut(graph)

if __name__ == '__main__':
    # file_name = 'GraphMinTest.txt'
    file_name = 'GraphMinCut.txt'

    with open(file_name) as f:
        adj_list = [list(map(int, v.split()))[1:] for v in f.readlines()]

    num_vertices = len(adj_list)
    graph = list()
    for vertex in range(num_vertices):
        for j in adj_list[vertex]:
            # smallest vertex number of an edge is assumed as the edge tail
            edge = sorted([vertex+1, j])
            if edge not in graph:
                graph.append(edge)

    s2 = time.time()
    # run iterations for at least N**2 times and remember the elite offspring results
    global_min_cut = num_vertices - 1
    gl_itr = -1
    num_runs = num_vertices**2
    # num_runs = int((num_vertices**2)*math.log(num_vertices))
    print('running the vanilla karger min-cut algorithm for {0} times'.format(num_runs))
    for i in range(num_runs):
        curr_min_cut = graph_min_cut(deepcopy(graph))
        global_min_cut = min(curr_min_cut, global_min_cut)
        if global_min_cut == curr_min_cut:
            gl_itr = i
        print(' ITR #{0} global min-cut value found so far is {1} from itr #{2}'.format(i, global_min_cut, gl_itr))
    e2 = time.time()

    print('MIN-CUT value is...', global_min_cut)

    time2 = e2-s2
    print('graph partitioning time.......', round(time2, 6))