# noinspection PyUnresolvedReferences
from typing import *

import pytest


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    grid: List[List[int]]
    m: int
    n: int

    EMPTY = 0
    BRICK = 1
    STABLE = 2
    FALL = 3

    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]):
        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])

        # hit
        for i, j in hits:
            grid[i][j] -= 1

        # mark
        for i in range(self.m):
            mark = self.STABLE if i == 0 else self.FALL  # stable if on top row
            for j in range(self.n):
                if self.grid[i][j] == self.BRICK:
                    self.dfs_mark((i, j), mark)

        falls = []
        # reverse hit
        for i, j in reversed(hits):
            self.grid[i][j] += 1
            if self.grid[i][j] == self.BRICK:
                self.grid[i][j] = self.FALL
                if i == 0 or any(
                    map(
                        lambda p: self.grid[p[0]][p[1]] == self.STABLE,
                        self.neighbors(i, j),
                    )
                ):
                    falls.append(
                        self.dfs_mark((i, j), mark=self.STABLE, old_mark=self.FALL) - 1
                    )
                else:
                    falls.append(0)
            else:
                falls.append(0)

        return list(reversed(falls))

    def dfs_mark(self, top_point, mark, old_mark=BRICK):
        cnt = 0
        stack = [top_point]
        while stack:
            x, y = stack.pop()
            if self.grid[x][y] == old_mark:
                self.grid[x][y] = mark
                cnt += 1
                stack.extend(self.neighbors(x, y))
        return cnt

    def neighbors(self, x, y):
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.m and 0 <= ny < self.n:
                yield nx, ny


_cases = [
    (([[1, 0, 0, 0], [1, 1, 1, 0]], [[1, 0]]), [2]),
    (([[1, 0, 0, 0], [1, 1, 0, 0]], [[1, 1], [1, 0]]), [0, 0]),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol803(inputs, expected):
    sol = Solution()
    output = sol.hitBricks(*inputs)
    assert output == expected
