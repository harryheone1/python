from typing import List


class UnionFind:
    def __init__(self, equations: List[List[str]], values: List[float]):
        self.parents = dict()
        for idx, equation in enumerate(equations):
            self.parents[equation[0]] = (equation[0], 1.0)
            self.parents[equation[1]] = (equation[1], 1.0)
            self.union(equation[0], equation[1], values[idx])

    def find_root(self, code: str) -> tuple:
        if code not in self.parents.keys():
            return None, None
        ratio = self.parents[code][1]
        while self.parents[code][0] != code:
            code = self.parents[code][0]
            ratio = ratio * self.parents[code][1]
        return (code, ratio)

    def connect(self, code1: str, code2: str) -> float:
        root1, ratio1 = self.find_root(code1)
        root2, ratio2 = self.find_root(code2)
        if root1 and root2 and root1 == root2:
            return ratio1 / ratio2

        return -1.0

    def union(self, code1: str, code2: str, ratio: float):
        root1, ratio1 = self.find_root(code1)
        root2, ratio2 = self.find_root(code2)
        # c1/r1 = ratio1, c2/r2 = ratio2, c1/c2 = ratio, so r1/r2 = ratio2/ratio1 * ratio
        root_ratio = ratio2 / ratio1 * ratio
        self.parents[root1] = (root2, root_ratio)


class Solution:

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = UnionFind(equations, values)
        res = list()
        # return uf.parents
        for query in queries:
            ratio = uf.connect(query[0], query[1])
            res.append(ratio)
        return res

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

wrapper = Solution()
wrapper.calcEquation(equations, values, queries)

