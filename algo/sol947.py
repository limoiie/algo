# noinspection PyUnresolvedReferences
from typing import *

import pytest


class UnionFind:
    def __init__(self):
        self.parent = dict()

    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            self.parent[pi] = pj

    def find(self, i):
        self.parent.setdefault(i, i)
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        ufind = UnionFind()

        same_row = dict()
        same_col = dict()

        for x, y in stones:
            same_row.setdefault(x, []).append(y)
            same_col.setdefault(y, []).append(x)

        for x, ys in same_row.items():
            for i in range(len(ys) - 1):
                ufind.union((x, ys[i]), (x, ys[i + 1]))

        for y, xs in same_col.items():
            for i in range(len(xs) - 1):
                ufind.union((xs[i], y), (xs[i + 1], y))

        roots = set()
        for x, y in stones:
            roots.add(ufind.find((x, y)))
        return len(stones) - len(roots)


_cases = [
    (([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]],), 5),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol947(inputs, expected):
    sol = Solution()
    output = sol.removeStones(*inputs)
    assert output == expected
