from collections import deque
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []

        result = []
        queue: deque[tuple[TreeNode, int]] = deque([(root, 0)])
        levels_sum: dict[int, float] = {}
        levels_count: dict[int, float] = {}

        while len(queue) > 0:
            tree_node, level = queue.popleft()
            levels_sum[level] = levels_sum.get(level, 0) + tree_node.val
            levels_count[level] = levels_count.get(level, 0) + 1

            if tree_node.left:
                queue.append((tree_node.left, level+1))
            if tree_node.right:
                queue.append((tree_node.right, level+1))

        for level, count in levels_count.items():
            result.append(levels_sum[level]/count)

        return result
