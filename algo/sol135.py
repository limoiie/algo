from typing import *

import pytest


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i] and candies[i - 1] >= candies[i]:
                candies[i] = candies[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i + 1] < ratings[i] and candies[i + 1] >= candies[i]:
                candies[i] = candies[i + 1] + 1
        return sum(candies)


_cases = [
    (([1, 0, 2],), 5),
    (([1, 2, 2],), 4),
    (([1, 3, 2, 2, 1],), 7),
    (([1, 3, 4, 5, 2],), 11),
    (([1, 2, 3, 1, 0],), 9),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol135(inputs, expected):
    sol = Solution()
    output = sol.candy(*inputs)
    assert output == expected
