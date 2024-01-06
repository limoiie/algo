# noinspection PyUnresolvedReferences
from typing import *

import pytest


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    grid: List[List[int]]
    n: int

    def largestIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.n = len(grid)

        counter = {0: 0}
        base = 0x10
        for i in range(self.n):
            for j in range(self.n):
                if grid[i][j] == 1:
                    counter[base] = self.dfs(i, j, base)
                    base += 1

        ans = max(counter.values())
        for i in range(self.n):
            for j in range(self.n):
                if grid[i][j] == 0:
                    bases = set(map(lambda p: grid[p[0]][p[1]], self.neighbors(i, j)))
                    ans = max(ans, 1 + sum(map(counter.get, bases)))
        return ans

    def dfs(self, x, y, color):
        cnt = 0
        stack = [(x, y)]
        while stack:
            x, y = stack.pop()
            if self.grid[x][y] == 1:
                self.grid[x][y] = color
                cnt += 1
                for p in self.neighbors(x, y):
                    stack.append(p)
        return cnt

    def neighbors(self, x, y):
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n:
                yield nx, ny


_cases = [
    (([[1, 0], [0, 1]],), 3),
    (([[1, 1], [0, 1]],), 4),
    (([[1, 1], [1, 1]],), 4),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol827(inputs, expected):
    sol = Solution()
    output = sol.largestIsland(*inputs)
    assert output == expected
