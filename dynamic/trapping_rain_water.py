from collections import deque
from typing import List, Optional


class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0

        left_max = [0] * len(height)
        right_max = [0] * len(height)

        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i-1])

        for i in range(len(height)-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i+1])

        for i in range(0, len(height)):
            volume = min(left_max[i], right_max[i])-height[i]
            if volume > 0:
                result += volume

        return result



