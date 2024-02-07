import itertools

# noinspection PyUnresolvedReferences
from typing import *

import pytest

# noinspection PyUnresolvedReferences
from algo.datatypes import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        for i, j in itertools.chain(
            itertools.product([0, m - 1], range(n)),
            itertools.product(range(1, m - 1), [0, n - 1]),
        ):
            if visited[i][j] or board[i][j] != "O":
                continue

            bag = [(i, j)]
            while bag:
                x, y = bag.pop()
                visited[x][y], board[x][y] = True, "-"
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= (nx := x + dx) < m and 0 <= (ny := y + dy) < n:
                        if not visited[nx][ny] and board[nx][ny] == "O":
                            bag.append((nx, ny))

        for i, j in itertools.product(range(m), range(n)):
            if board[i][j] == "-":
                board[i][j] = "O"
            elif board[i][j] == "O":
                board[i][j] = "X"


_cases = [
    ((),),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol130(inputs, expected):
    sol = Solution()
    output = sol.solve(*inputs)
    assert output == expected
