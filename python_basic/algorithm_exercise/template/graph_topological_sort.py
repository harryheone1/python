# Leetcode 210 - DFS
from collections import defaultdict
from typing import List


def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    # General adjacent list
    graph = defaultdict(list)

    # 0 - not start yet to search
    # 1 - in progress of search
    # 2 - finished of search
    visited = [0 for _ in range(numCourses + 1)]

    # build graph
    for prerequisite in prerequisites:
        graph[prerequisite[0]].append(prerequisite[1])
    # Sentinel - don't need loop any more
    graph[numCourses] = [course for course in range(numCourses)]

    def recursive(course: int):
        # connect_to a vertex in progress, circle and not valid
        if visited[course] == 1: return False
        # connect_to a vertex finished, 剪枝 purge
        if visited[course] == 2: return True

        visited[course] = 1
        for dependency in graph[course]:
            if not recursive(dependency): return False
        visited[course] = 2
        res.append(course)
        return True

    # check all course
    res = list()
    recursive(numCourses)
    return res[0: numCourses] if len(res) == numCourses + 1 else []

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # BFS
        # build in_degree of each node, need to know which node's indegree is 0 - time complexity O(1)
        # remove node with 0 in_degree, update other node's indegree
        # repeat, if all nodes indegree is higher than 0, there is circle.

        in_degree = [0 for _ in range(numCourses)]
        zero_degree_course = deque()
        graph = defaultdict(list)

        for prerequisite in prerequisites:
            in_degree[prerequisite[1]] += 1
            graph[prerequisite[0]].append(prerequisite[1])

        for course in range(len(in_degree)):
            if in_degree[course] == 0: zero_degree_course.append(course)

        res = list()

        while zero_degree_course:
            course = zero_degree_course.popleft()
            res.append(course)

            for dependency in graph[course]:
                in_degree[dependency] -= 1
                if in_degree[dependency] == 0:
                    zero_degree_course.append(dependency)

        return res[::-1] if len(res) == numCourses else []