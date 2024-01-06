# noinspection PyUnresolvedReferences
from typing import *

import pytest


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        self.parents[self.find(x)] = self.find(y)


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]):
        n = len(graph)
        ufind = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 1:
                    ufind.union(i, j)

        cnt = dict()
        for i in range(n):
            root_i = ufind.find(i)
            cnt.setdefault(root_i, 0)
            cnt[root_i] += 1

        duplicates = set()
        init_roots = dict()
        for i in initial:
            root_i = ufind.find(i)
            if root_i in init_roots:
                if root_i not in duplicates:
                    duplicates.add(root_i)
            else:
                init_roots[root_i] = i

        values = []
        for root, i in init_roots.items():
            if root in duplicates:
                continue
            values.append((-cnt[root], i))

        if not values:
            return min(initial)
        return min(values)[1]


_cases = [
    (([[1, 1, 0], [1, 1, 0], [0, 0, 1]], [0, 1]), 0),
    (([[1, 0, 0], [0, 1, 0], [0, 0, 1]], [0, 2]), 0),
    (([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 2]), 1),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol924(inputs, expected):
    sol = Solution()
    output = sol.minMalwareSpread(*inputs)
    assert output == expected
