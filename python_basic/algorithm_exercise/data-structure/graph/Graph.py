class Graph:
    def __init__(self, nums_vertex: int):
        self._nums_vertex = nums_vertex
        self._adjacency_list = [[] for _ in range(nums_vertex)]

    def add_edge(self, src: int, des: int) -> bool:
        if src < self._nums_vertex and des < self._nums_vertex:
            self._adjacency_list[src].append(des)
            return True
        return False

    def delete_edge(self, src: int, des: int) -> bool:
        # TODO
        return False

    def bfs(self, s: int, t: int) -> list:
        # TODO
        return list()

    def dfs(self, s: int, t: int) -> list:
        path = []
        visited = [False for _ in range(self._nums_vertex)]

        def dfs_re(s: int):

            if s == t:
                path.append(t)
                return True

            if visited[s]:
                return False

            path.append(s)
            visited[s] = True
            for v in self._adjacency_list[s]:
                if dfs_re(v): return True

            path.pop()
            visited[s] = False

        dfs_re(s)
        return path


if __name__ == '__main__':
    graph = Graph(7)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(4, 6)
    graph.add_edge(5, 6)
    print(graph.dfs(0, 6))
