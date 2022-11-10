class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        previous_step = 1
        last_step = 2
        current_step = 0

        for i in range(2, n):
            current_step = previous_step + last_step
            previous_step = last_step
            last_step = current_step

        return current_step