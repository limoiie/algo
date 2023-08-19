from typing import *

import pytest


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                profit += prices[i] - prices[i - 1]
        return profit


_cases = [
    (([7, 1, 5, 3, 6, 4],), 7),
    (([1, 2, 3, 4, 5],), 4),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol122(inputs, expected):
    sol = Solution()
    output = sol.maxProfit(*inputs)
    assert output == expected
