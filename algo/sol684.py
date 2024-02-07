# noinspection PyUnresolvedReferences
from typing import *

import pytest

# noinspection PyUnresolvedReferences
from algo.datatypes import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    class UnionFind:
        def __init__(self, n):
            self._prev = list(range(n))

        def union(self, p, q):
            pi = self.find(p)
            qi = self.find(q)
            if pi == qi:
                return True

            self._prev[pi] = qi

        def find(self, x):
            if self._prev[x] != x:
                self._prev[x] = self.find(self._prev[x])
            return self._prev[x]

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        u_find = self.UnionFind(len(edges) + 1)
        for x, y in edges:
            if u_find.union(x, y):
                return [x, y]
        raise RuntimeError()


_cases = [
    (([[1, 2], [1, 3], [2, 3]],), [2, 3]),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol684(inputs, expected):
    sol = Solution()
    output = sol.findRedundantConnection(*inputs)
    assert output == expected
