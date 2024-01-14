from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        backtrace(board, 0)


stubs = "123456789"


def backtrace(board, i):
    i, x, y = find_empty(board, i)
    if i is None:
        return True

    for v in stubs:
        if is_valid(board, x, y, v):
            board[x][y] = v
            if backtrace(board, i):
                return True
            board[x][y] = "."
    return False


def find_empty(board, i):
    for i in range(i, 81):
        x, y = i // 9, i % 9
        if board[x][y] == ".":
            return i, x, y
    return None, None, None


def is_valid(board, x, y, val):
    for i in range(9):
        if board[x][i] == val:
            return False
        if board[i][y] == val:
            return False
        if board[(x // 3) * 3 + i // 3][(y // 3) * 3 + i % 3] == val:
            return False
    return True


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(
        args=(
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
        ),
        expected=...,
    ),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    sol.solveSudoku(*case.args)
    print(case.args)
