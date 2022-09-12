import collections
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # bfs (i, j, count of obstacles): queue
        queue = collections.deque([])
        m = len(grid)
        n = len(grid[0])
        queue.append((0, 0, grid[0][0], 0))
        visited = set()
        while queue:
            print(len(queue))
            i, j, obs, depth = queue.popleft()
            print(depth)
            obs += grid[i][j]
            if obs > k:
                continue
            if (i, j, obs) in visited:
                continue
            visited.add((i, j, obs))
            if i == m - 1 and j == n - 1:
                return depth

            if i > 0:
                queue.append((i - 1, j, obs, depth + 1))
            if i < m - 1:
                queue.append((i + 1, j, obs, depth + 1))
            if j > 0:
                queue.append((i, j - 1, obs, depth + 1))
            if j < n - 1:
                queue.append((i, j + 1, obs, depth + 1))
        return -1


test = Solution()
grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1], [1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0],
        [0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0]]
k = 27
print(test.shortestPath(grid, k))