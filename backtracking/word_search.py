from typing import List, Optional


class Solution:
    board: List[List[str]]
    used: set

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board

        for row in range(0, len(self.board)):
            for col in range(0, len(self.board[row])):
                self.used = set()
                result = self.find(row, col, word)

                if result:
                    return result
        return False

    def find(self, row, col, word) -> bool:
        if (row, col) in self.used:
            return False

        if self.board[row][col] != word[0]:
            return False

        self.used.add((row, col))

        if len(word) == 1:
            return True

        # check left
        check_left = False
        if col > 0:
            check_left = self.find(row, col-1, word[1:])

        # check right
        check_right = False
        if col < len(self.board[row])-1:
            check_right = self.find(row, col+1, word[1:])

        # check top
        check_top = False
        if row > 0:
            check_top = self.find(row-1, col, word[1:])

        # check bottom
        check_bottom = False
        if row < len(self.board)-1:
            check_bottom = self.find(row+1, col, word[1:])

        if True in (check_left, check_right, check_top, check_bottom):
            return True

        self.used.remove((row, col))
        return False






