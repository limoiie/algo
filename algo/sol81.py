# noinspection PyUnresolvedReferences
from typing import *

import pytest

# noinspection PyUnresolvedReferences
from algo.datatypes import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        tail = nums[0]
        while r >= 0:
            if nums[r] != tail:
                tail = nums[r]
                break
            r -= 1

        if target == nums[l] or target == nums[r]:
            return True

        while l <= r:
            m = (l + r) >> 1
            if target == nums[m]:
                return True

            if target < nums[m]:
                if target <= tail < nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] <= tail < target:
                    r = m - 1
                else:
                    l = m + 1
        return False


_cases = [
    (([2, 5, 6, 0, 0, 1, 2], 0), True),
    (([2, 5, 6, 0, 0, 1, 2], 3), False),
    (([1, 0, 1, 1, 1], 0), True),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol81(inputs, expected):
    sol = Solution()
    output = sol.search(*inputs)
    assert output == expected
