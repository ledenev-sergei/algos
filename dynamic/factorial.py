import timeit
import logging as log


class Solution:
    def recursive(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        return n * self.recursive(n-1)

    def nonRecursive(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        result = 1

        for current_n in range(1, n+1):
            result = result * current_n

        return result


if __name__ == "__main__":
    def run_non_recursive():
        solution = Solution()
        solution.nonRecursive(100)

    def run_recursive():
        solution = Solution()
        solution.recursive(100)

    print("Non recursive:", timeit.timeit(run_non_recursive, number=10000))
    print("Recursive:", timeit.timeit(run_non_recursive, number=10000))
