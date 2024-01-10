import math

# noinspection PyUnresolvedReferences
from typing import *

import pytest


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        # self.sizes = [1] * n

    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            # if self.sizes[pj] < self.sizes[pi]:
            #     pi, pj = pj, pi
            self.parents[pi] = pj
            # self.sizes[pj] += self.sizes[pi]


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def largestComponentSize(self, nums: List[int]):
        n = max(nums) + 1
        ufind = UnionFind(n)

        for k in nums:
            for p in range(2, int(math.sqrt(n)) + 1):
                if p == k:
                    continue
                if k % p == 0:
                    ufind.union(p, k)
                    ufind.union(k // p, k)

        ans = 0
        counts = dict()
        for k in nums:
            root_k = ufind.find(k)
            counts[root_k] = counts.get(root_k, 0) + 1
            ans = max(ans, counts[root_k])
        return ans


_cases = [(([1, 2, 3, 4, 5, 6, 7, 8, 9],), 6), (([1, 2],), 1)]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol952(inputs, expected):
    sol = Solution()
    output = sol.largestComponentSize(*inputs)
    assert output == expected
