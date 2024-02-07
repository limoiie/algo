# noinspection PyUnresolvedReferences
from typing import *

import pytest

# noinspection PyUnresolvedReferences
from algo.datatypes import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        p = s + "-" + s[::-1]
        find = [0] * len(p)

        for i in range(len(p)):
            if i == 0:
                continue

            t = find[i - 1]
            while t > 0 and p[i] != p[t]:
                t = find[t - 1]
            if p[i] == p[t]:
                t += 1

            find[i] = t

        l = find[-1]
        return s[: l - 1 : -1] + s


_cases = [
    (("aacecaaa",), "aaacecaaa"),
    (("abcd",), "dcbabcd"),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol214(inputs, expected):
    sol = Solution()
    output = sol.shortestPalindrome(*inputs)
    assert output == expected
