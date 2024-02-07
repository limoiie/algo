# noinspection PyUnresolvedReferences
from typing import *

import pytest

# noinspection PyUnresolvedReferences
from algo.datatypes import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[0][0] = True

        for pi, pc in enumerate(p):
            if pc == "*":
                pc = p[pi - 1]
                dp[pi + 1][0] = dp[pi - 1][0]
                for si, sc in enumerate(s):
                    dp[pi + 1][si + 1] = (
                        (pc == sc or pc == ".") and (dp[pi][si] or dp[pi + 1][si])
                        or (dp[pi - 1][si + 1])
                    )
            else:
                for si, sc in enumerate(s):
                    dp[pi + 1][si + 1] = (
                        (pc == sc or pc == ".") and dp[pi][si]
                    )

        return dp[-1][-1]


_cases = [
    (("aab", "c*a*b"), True),
    (("aa", "aaa"), False),
    (("aa", "a"), False),
    (("aa", "a*"), True),
    (("ab", ".*"), True),
    (("mississippi", "mis*is*ip*."), True),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol10(inputs, expected):
    sol = Solution()
    output = sol.isMatch(*inputs)
    assert output == expected
