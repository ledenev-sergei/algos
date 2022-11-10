from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[0])):
                if matrix[row][col] == 0:
                    self.empty_row_except_zero(matrix, row)
                    self.empty_col_except_zero(matrix, col)

        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[0])):
                if matrix[row][col] is None:
                    matrix[row][col] = 0

    def empty_row_except_zero(self, matrix, row: int):
        for col in range(0, len(matrix[row])):
            if matrix[row][col] != 0:
                matrix[row][col] = None

    def empty_col_except_zero(self, matrix, col: int):
        for row in range(0, len(matrix)):
            if matrix[row][col] != 0:
                matrix[row][col] = None