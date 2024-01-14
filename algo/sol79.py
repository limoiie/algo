from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if backtrace(board, word, i, j, visited, m, n):
                    return True
        return False


def backtrace(board, word, x, y, visited, m, n, k=0):
    if board[x][y] != word[k]:
        return False
    if k == len(word) - 1:
        return True

    visited[x][y] = True
    for nx, ny in neighbors(visited, m, n, x, y):
        if backtrace(board, word, nx, ny, visited, m, n, k + 1):
            return True
    visited[x][y] = False


def neighbors(visited, m, n, x, y):
    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
            yield nx, ny


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([["a"]], "a"), expected=True),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.exist(*case.args)
    assert output == case.expected
