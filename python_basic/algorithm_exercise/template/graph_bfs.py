from collections import deque


class Vertex:
    def __init__(self, val):
        self.val = val
        self.adjacent = []


class Graph:
    def __init__(self, n: int, sparse: bool):
        if sparse:
            self.adjacent_list = [[] for i in range(n)]
        else:
            self.adjacent_matrix = [[False for _ in range(n)] for i in range(n)]

    def add_edge(self, from_v: int, to_v: int):
        if self.adjacent_list:
            self.adjacent_list[from_v] = to_v
        if self.adjacent_matrix:
            self.adjacent_matrix[from_v][to_v] = True


"""
procedure BFS(G, v):
    create a queue Q
    enqueue v onto Q
    mark v
    while Q is not empty:
        t <- Q.deque()
        if t is what we are looking for:
            return t
        for all edges e in G.adjacentEdges(t) do:
            u <- G.adjacentvertex(t, e)
            if u is not marked:
                mark u
                enqueue u onto Q
"""


def bfs(start: Vertex, end: Vertex):
    queue = deque()
    visited = set()
    queue.append(start)
    visited.add(start)
    step = 0

    while queue:
        for _ in range(len(queue)):
            vertex = queue.popleft()
            if vertex.val == end.val:
                return step
            for union in vertex.adjacent:
                if union is not visited:
                    queue.append(union)
                    visited.add(union)
        step += 1
