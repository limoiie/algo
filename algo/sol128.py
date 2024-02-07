# noinspection PyUnresolvedReferences
from typing import *

import pytest

# noinspection PyUnresolvedReferences
from algo.datatypes import *


class UnionFind:
    def __init__(self):
        pass


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        prev = dict()
        for n in nums:
            prev.setdefault(n, n)
            if n - 1 in prev:
                prev[n] = n - 1
            if n + 1 in prev:
                prev[n + 1] = n

        counts = dict()

        def find(x):
            if prev[x] != x:
                prev[x], cnt = find(prev[x])
                counts.setdefault(x, cnt + 1)
            return prev[x], counts.setdefault(x, 1)

        ans = 0
        for n in nums:
            p, c = find(n)
            ans = max(ans, c)
        return ans


_cases = [
    (([100, 4, 200, 1, 3, 2],), 4),
    (([0, 3, 7, 2, 5, 8, 4, 6, 0, 1],), 9),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol128(inputs, expected):
    sol = Solution()
    output = sol.longestConsecutive(*inputs)
    assert output == expected
