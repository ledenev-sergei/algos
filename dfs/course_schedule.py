from typing import List, Optional


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]

        for x, y in prerequisites:
            graph[x].append(y)

        def dfs(i: int):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True

            # mark current visiting node
            visit[i] = -1

            for j in graph[i]:
                if not dfs(j):
                    return False

            # mark node is visited
            visit[i] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True








