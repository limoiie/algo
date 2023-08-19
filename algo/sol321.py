from typing import *

import pytest


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        pass


_cases = [
    (([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5), [9, 8, 6, 5, 3]),
    (([6, 7], [6, 0, 4], 5), [6, 7, 6, 0, 4]),
    (([3, 9], [8, 9], 3), [9, 8, 9]),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol321(inputs, expected):
    sol = Solution()
    output = sol.maxNumber(*inputs)
    assert output == expected
