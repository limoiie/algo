# noinspection PyUnresolvedReferences
from typing import *

import pytest

# noinspection PyUnresolvedReferences
from algo.datatypes import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def fn(curr, opened, remain):
            if remain == 0 and opened == 0:
                ans.append(curr)
                return

            if remain != 0:
                fn(curr + "(", opened + 1, remain - 1)
            if opened != 0:
                fn(curr + ")", opened - 1, remain)

        fn("", 0, n)
        return ans


_cases = [
    ((3,), ["((()))", "(()())", "(())()", "()(())", "()()()"]),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol22(inputs, expected):
    sol = Solution()
    output = sol.generateParenthesis(*inputs)
    assert output == expected
