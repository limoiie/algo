# noinspection PyUnresolvedReferences
from typing import *

import pytest

# noinspection PyUnresolvedReferences
from algo.datatypes import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def nthUglyNumber(self, n: int):
        ugly = [1]
        i2 = i3 = i5 = 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            u_min = min(u2, u3, u5)
            if u_min == u2:
                i2 += 1
            if u_min == u3:
                i3 += 1
            if u_min == u5:
                i5 += 1
            ugly.append(u_min)
            n -= 1
        return ugly[-1]


_cases = [
    ((),),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol264(inputs, expected):
    sol = Solution()
    output = sol.nthUglyNumber(*inputs)
    assert output == expected
