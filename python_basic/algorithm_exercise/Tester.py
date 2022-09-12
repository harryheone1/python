import copy

class Solution:
    def __init__(self, num_vertices: int):
        self._N = 1

    def solveNQueens(self, n: int):
        res = []
        path = [['.' for i in range(n)] for j in range(n)]

        def isValid(row, col) -> bool:
            for i in range(1, n + 1):
                if col + i < n and path[row][col + i] == 'Q':
                    return False
                if col - i >= 0 and path[row][col - i] == 'Q':
                    return False
                if row + i < n and path[row + i][col] == 'Q':
                    return False
                if row - i >= 0 and path[row - i][col] == 'Q':
                    return False
                if row + i < n and col + i < n and path[row + i][col + i] == 'Q':
                    return False
                if row - i >= 0 and col - i >= 0 and path[row - i][col - i] == 'Q':
                    return False
                if row + i < n and col - i >= 0 and path[row + i][col - i] == 'Q':
                    return False
                if row - i >= 0 and col + i < n and path[row - i][col + i] == 'Q':
                    return False
            return True

        def placeQueen(r: int) -> None:
            if r == 0:
                res.append(copy.deepcopy(path))
                return
            for i in range(n):
                if isValid(r - 1, i):
                    path[r - 1][i] = 'Q'
                    placeQueen(r - 1)
                    path[r - 1][i] = '.'

        placeQueen(n)
        return res



if __name__ == "__main__":
    graph = Solution(8)
    print(graph.solveNQueens(1))
    print(graph.solveNQueens(2))
    print(graph.solveNQueens(4))

