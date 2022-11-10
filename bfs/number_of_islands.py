from collections import deque
from typing import List, Set, Tuple

"""
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
"""


class Solution:
    visited_nodes: Set[Tuple[int, int]]
    number_of_islands: int

    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited_nodes = set()
        self.number_of_islands = 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if (i, j) in self.visited_nodes:
                    continue

                if grid[i][j] == "1":
                    self.number_of_islands += 1
                    self._visit_island(grid, (i, j))

        return self.number_of_islands

    def _visit_island(self, grid: List[List[str]], start_from: Tuple[int, int]):
        visit_queue: deque[tuple[int, int]] = deque([start_from])

        while len(visit_queue) > 0:
            current_node = visit_queue.popleft()
            current_node_i, current_node_j = current_node
            if current_node in self.visited_nodes:
                continue

            self.visited_nodes.add(current_node)

            # check top node
            if 0 < current_node_i < len(grid):
                top_node_i = current_node_i - 1
                top_node_j = current_node_j
                if (top_node_i, top_node_j) not in self.visited_nodes and grid[top_node_i][top_node_j] == "1":
                    visit_queue.append((top_node_i, top_node_j))

            # check down node
            if current_node_i < len(grid) - 1:
                down_node_i = current_node_i + 1
                down_node_j = current_node_j
                if (down_node_i, down_node_j) not in self.visited_nodes and grid[down_node_i][down_node_j] == "1":
                    visit_queue.append((down_node_i, down_node_j))

            # check left node
            if 0 < current_node_j < len(grid[current_node_i]):
                left_node_i = current_node_i
                left_node_j = current_node_j - 1
                if (left_node_i, left_node_j) not in self.visited_nodes and grid[left_node_i][left_node_j] == "1":
                    visit_queue.append((left_node_i, left_node_j))

            # check right node
            if current_node_j < len(grid[current_node_i]) - 1:
                right_node_i = current_node_i
                right_node_j = current_node_j + 1
                if (right_node_i, right_node_j) not in self.visited_nodes and grid[right_node_i][right_node_j] == "1":
                    visit_queue.append((right_node_i, right_node_j))

