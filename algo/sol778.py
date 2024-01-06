# noinspection PyUnresolvedReferences
import heapq
from typing import *

import pytest


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def swimInWater(self, grid: List[List[int]]):
        n = len(grid)
        max_int = n * n + 1

        t = 0
        boundaries = [(grid[0][0], 0, 0)]
        grid[0][0] = max_int

        while boundaries:
            elevation, i, j = heapq.heappop(boundaries)
            t = max(t, elevation)
            if i == n - 1 and j == n - 1:
                break

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] != max_int:
                    heapq.heappush(boundaries, (grid[ni][nj], ni, nj))
                    grid[ni][nj] = max_int

        return t


_cases = [
    (([[0, 2], [1, 3]],), 3),
    (
        (
            [
                [0, 1, 2, 3, 4],
                [24, 23, 22, 21, 5],
                [12, 13, 14, 15, 16],
                [11, 17, 18, 19, 20],
                [10, 9, 8, 7, 6],
            ],
        ),
        16,
    ),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol778(inputs, expected):
    sol = Solution()
    output = sol.swimInWater(*inputs)
    assert output == expected
