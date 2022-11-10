from typing import List, Optional


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> list[int]:
        graph = [[] for _ in range(numCourses)]

        for course, required_course in prerequisites:
            graph[course].append(required_course)

        result = []
        visited = [0 for _ in range(numCourses)]

        def dfs(start_course) -> bool:
            if visited[start_course] == -1:  # course was already visited -> cycle in graph
                return False

            visited[start_course] = -1  # mark as visited

        for start_course in range(numCourses):
            if not dfs(start_course):
                return []

        return result











