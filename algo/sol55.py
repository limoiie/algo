from typing import *

import pytest


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i] + i, nums[i - 1])
        idx = 0
        while idx < len(nums) - 1:
            if nums[idx] == idx:
                return False
            idx = nums[idx]
        return True


_cases = [
    (([2, 3, 1, 1, 4],), True),
    (([3, 2, 1, 0, 4],), False),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol55(inputs, expected):
    sol = Solution()
    output = sol.canJump(*inputs)
    assert output == expected
