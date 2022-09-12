class DSU:

    """"
    Data structure design:
    N is number of nodes, each node has an index between [0, N - 1]
    Each node has a POINTER to its parents
    Union Find is a forest consists of a few trees
    At the beginning, there is NO connected node; For each node, their parents are themselves
    """
    def __init__(self, N: int):
        # count of tree
        self.count = N
        # size of each tree - to have a balanced tree
        self.size = list()

        # parent node of each node
        self.parent = list()
        for i in range(N):
            self.parent.append(i)
            self.size.append(1)

    # check if two nodes are connected
    def connected(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        return root_x == root_y

    # find root node of the input node with index x
    def find(self, x: int) -> int:
        # only the root node, its parent will be itself.
        while self.parent[x] != x:
            # before: x -> father -> grand_father
            # after:    grand_father
            #       x               parent
            # make the tree depth to be constant -> like the B-trees, it should be fat and short
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]

        return x

    # connect two nodes with index x and y
    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        # previous version:
        # self.parent[root_x] = root_y


        # attach smaller tree to bigger tree to make the tree be more balanced
        # time complexity of all operations depends on the depth of the tree
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]

        self.count -= 1

    def count_tree(self) -> int:
        return self.count


dsu = DSU(10)
print(dsu.find(1))
print(dsu.count_tree())

""""
    2
1
"""
dsu.union(1, 2)
print(dsu.find(1))
print(dsu.count_tree())


""""
        3
    4        5
    
        3
    4   1   5
        2
"""
dsu.union(3, 4)
dsu.union(3, 5)
dsu.union(2, 4)
print(dsu.find(5))
print(dsu.find(1))
print(dsu.count_tree())