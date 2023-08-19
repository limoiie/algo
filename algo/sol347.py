import heapq
from collections import defaultdict

# noinspection PyUnresolvedReferences
from typing import *

import pytest


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        pair = heapq.nlargest(k, counts.items(), key=lambda p: p[1])
        return [p[0] for p in pair]


_cases = [
    (([1, 1, 1, 2, 2, 3], 2), [1, 2]),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol347(inputs, expected):
    sol = Solution()
    output = sol.topKFrequent(*inputs)
    assert output == expected
