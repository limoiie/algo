from typing import *

import pytest


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            lh, rh = height[l], height[r]
            max_area = max(max_area, min(lh, rh) * (r - l))
            if lh <= rh:
                l += 1
            if lh >= rh:
                r -= 1

        return max_area


_cases = [
    (([1, 8, 6, 2, 5, 4, 8, 3, 7],), 49),
    (([1, 1],), 1),
    (([8, 10, 14, 0, 13, 10, 9, 9, 11, 11],), 80),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol11(inputs, expected):
    sol = Solution()
    output = sol.maxArea(*inputs)
    assert output == expected
