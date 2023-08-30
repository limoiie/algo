# noinspection PyUnresolvedReferences
from typing import *

import pytest

# noinspection PyUnresolvedReferences
from algo.datatypes import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def isUgly(self, n: int):
        if n <= 0:
            return False
        while (n % 2) == 0:
            n //= 2
        while (n % 3) == 0:
            n //= 3
        while (n % 5) == 0:
            n //= 5
        return n == 1


_cases = [
    ((),),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol263(inputs, expected):
    sol = Solution()
    output = sol.isUgly(*inputs)
    assert output == expected
