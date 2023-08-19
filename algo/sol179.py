from functools import cmp_to_key
from typing import *

import pytest


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(l, r):
            lr, rl = l + r, r + l
            if lr > rl:
                return -1
            elif lr < rl:
                return 1
            else:
                return 0

        sorted_nums = sorted(map(str, nums), key=cmp_to_key(cmp))
        return "".join(sorted_nums)


_cases = [
    (([10, 2],), "210"),
    (([3, 30, 34, 5, 9],), "9534330"),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol179(inputs, expected):
    sol = Solution()
    output = sol.largestNumber(*inputs)
    assert output == expected
