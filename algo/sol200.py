# noinspection PyUnresolvedReferences
from typing import *

import pytest


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(x, y):
            stack = [(x, y)]
            while stack:
                x, y = stack.pop()
                if x < 0 or x >= n or y < 0 or y >= m:
                    continue

                if grid[x][y] == "1":
                    grid[x][y] = ""
                    stack.append((x - 1, y))
                    stack.append((x + 1, y))
                    stack.append((x, y - 1))
                    stack.append((x, y + 1))

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)
        return ans


_cases = [
    ((),),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol200(inputs, expected):
    sol = Solution()
    output = sol.numIslands(*inputs)
    assert output == expected
