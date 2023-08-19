from typing import *

import pytest


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def jump(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i] + i, nums[i - 1])
        idx, ans = 0, 0
        while idx < len(nums) - 1:
            idx = nums[idx]
            ans += 1
        return ans


_cases = [
    (([2, 3, 1, 1, 4],), 2),
    (([2, 3, 0, 1, 4],), 2),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol45(inputs, expected):
    sol = Solution()
    output = sol.jump(*inputs)
    assert output == expected
