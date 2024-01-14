from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        return backtrace(board, 0, [0] * n, [0] * n, [0] * (n + n), [0] * (n + n), n, n)


def backtrace(
    board, starting, row_slots, col_slots, slash_slots, backslash_slots, n, r
):
    if r == 0:
        return [list("".join(row) for row in board)]

    ans = []
    for i in range(starting, n * n):
        x, y = i // n, i % n
        if not is_valid(board, x, y, n):
            continue

        board[x][y] = "Q"
        ans += backtrace(
            board, i, row_slots, col_slots, slash_slots, backslash_slots, n, r - 1
        )
        board[x][y] = "."

    return ans


def is_valid(board, x, y, n):
    for i in range(n):
        if board[x][i] == "Q" or board[i][y] == "Q":
            return False
    for i in range(n):
        for j in range(n):
            if board[i][j] == "Q" and (i + j == x + y or i - j == x - y):
                return False
    return True


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(4,), expected=...),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.solveNQueens(*case.args)
    assert output == case.expected
