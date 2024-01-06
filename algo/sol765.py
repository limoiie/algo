# noinspection PyUnresolvedReferences
from typing import *

import pytest


class UnionFind:
    def __init__(self, n):
        self._parents = list(range(n))

    def union(self, i, j):
        self._parents[self.find(i)] = self.find(j)

    def find(self, i):
        return i if self._parents[i] == i else self.find(self._parents[i])


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def minSwapsCouples(self, row: List[int]):
        ufind = UnionFind(len(row) // 2)
        for i in range(0, len(row), 2):
            l, r = row[i] // 2, row[i + 1] // 2
            if l != r:
                ufind.union(l, r)

        counts = dict()
        for i in range(len(row) // 2):
            root = ufind.find(i)
            counts.setdefault(root, 0)
            counts[root] += 1

        ans = 0
        for root, cnt in counts.items():
            ans += cnt - 1
        return ans


_cases = [
    (([0, 2, 1, 3],), 1),
    (([3, 2, 0, 1],), 0),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol765(inputs, expected):
    sol = Solution()
    output = sol.minSwapsCouples(*inputs)
    assert output == expected
