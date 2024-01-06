# noinspection PyUnresolvedReferences
from typing import *

import pytest


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))

    def union(self, i, j):
        self.parents[self.find(i)] = self.find(j)

    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    strs: List[str]

    def numSimilarGroups(self, strs: List[str]) -> int:
        self.strs = strs
        n = len(self.strs)
        ufind = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if self.is_similar(i, j):
                    ufind.union(i, j)

        bases = set()
        for i in range(n):
            bases.add(ufind.find(i))
        return len(bases)

    def is_similar(self, i, j):
        l, r = self.strs[i], self.strs[j]
        if len(l) != len(r):
            return False

        diffs = []
        for i in range(len(l)):
            if l[i] != r[i]:
                diffs.append(i)
                if len(diffs) > 2:
                    return False
        if len(diffs) != 2:
            return len(diffs) == 0

        i, j = diffs
        return (l[i], l[j]) == (r[j], r[i])


_cases = [((["tars", "rats", "arts", "star"],), 2), ((["omv", "ovm"],), 1)]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol839(inputs, expected):
    sol = Solution()
    output = sol.numSimilarGroups(*inputs)
    assert output == expected
