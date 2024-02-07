import itertools

# noinspection PyUnresolvedReferences
from typing import *

import pytest

# noinspection PyUnresolvedReferences
from algo.datatypes import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    class UnionFind:
        def __init__(self, n: int):
            self._prev = list(range(n))

        def union(self, p, q):
            pi = self.find(p)
            qi = self.find(q)
            self._prev[pi] = qi

        def find(self, x):
            if self._prev[x] != x:
                self._prev[x] = self.find(self._prev[x])
            return self._prev[x]

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        u_find = self.UnionFind(n)
        for i, j in itertools.product(range(n), range(n)):
            if isConnected[i][j]:
                u_find.union(i, j)

        starts = set()
        for i in range(n):
            starts.add(u_find.find(i))

        return len(starts)


_cases = [
    ((),),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol547(inputs, expected):
    sol = Solution()
    output = sol.findCircleNum(*inputs)
    assert output == expected
