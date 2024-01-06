# noinspection PyUnresolvedReferences
from typing import *

import pytest


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    m: int
    n: int

    def maxAreaOfIsland(self, grid: List[List[int]]):
        self.m, self.n = len(grid), len(grid[0])
        ans = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    ans = max(self.dfs(grid, i, j), ans)
        return ans

    def dfs(self, grid, i: int, j: int):
        cnt = 1
        grid[i][j] = 0
        queue = [(i, j)]
        while queue:
            x, y = queue.pop()

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.m and 0 <= ny < self.n:
                    if grid[nx][ny] == 1:
                        cnt += 1
                        grid[nx][ny] = 0
                        queue.append((nx, ny))

        return cnt


_cases = [
    # (
    #     (
    #         [
    #             [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    #             [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    #             [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    #             [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    #             [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    #         ],
    #     ),
    #     6,
    # ),
    (
        (
            [
                [1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1],
                [0, 0, 0, 1, 1],
            ],
        ),
        4,
    ),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol695(inputs, expected):
    sol = Solution()
    output = sol.maxAreaOfIsland(*inputs)
    assert output == expected
