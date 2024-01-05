# noinspection PyUnresolvedReferences
from typing import *

import pytest

# noinspection PyUnresolvedReferences
from algo.datatypes import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def countPrimes(self, n: int):
        cnt = 0
        arr = [False] * n
        for i in range(2, n):
            if not arr[i]:
                continue

            cnt += 1
            for j in range(i + i, n, i):
                arr[j] = True

        return cnt


_cases = [
    ((),),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol204(inputs, expected):
    sol = Solution()
    output = sol.countPrimes(*inputs)
    assert output == expected
