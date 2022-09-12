from collections import deque


class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """

        def is_valid(row, col, cur_k):

            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and (
                row, col, cur_k) not in visited and (cur_k >= 0)

        if len(grid[0]) == 1 and len(grid) == 1:
            return 0
        queue = deque()
        queue.append((0, 0, k - grid[0][0]))
        visited = set()
        path = 0

        while queue:
            path += 1
            print(path)
            print(len(queue))
            for _ in range(len(queue)):
                row, col, p_k = queue.popleft()
                for nei_r, nei_c, cur_k in [(row - 1, col, p_k), (row + 1, col, p_k), (row, col - 1, p_k),
                                            (row, col + 1, p_k)]:
                    cur_k -= grid[nei_r][nei_c]
                    if is_valid(nei_r, nei_c, cur_k):
                        if nei_r == len(grid) - 1 and nei_c == len(grid[0]) - 1:
                            return path
                        queue.append((nei_r, nei_c, cur_k))
                        visited.add((nei_r, nei_c, cur_k))

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
