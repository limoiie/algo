# noinspection PyUnresolvedReferences
from typing import *

import pytest


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target == nums[-1]:
            return len(nums) - 1
        if target == nums[0]:
            return 0

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1


_cases = [
    (([5, 1, 2, 3, 4], 3), 3),
    (([2, 4, 7, 9, 0], 9), 3),
    (([1, 2, 3, 4, 5, 6, 7, 8], 4), 3),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol33(inputs, expected):
    sol = Solution()
    output = sol.search(*inputs)
    assert output == expected
