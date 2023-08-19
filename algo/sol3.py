# noinspection PyUnresolvedReferences
from typing import *

import pytest


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mem = {}
        max_len, start = 0, 0
        for i, c in enumerate(s):
            existing_i = mem.get(c, None)
            if existing_i is None:
                mem[c] = i
            else:
                for j in range(start, existing_i + 1):
                    mem.pop(s[j])
                mem[c] = i
                start = existing_i + 1
            max_len = max(max_len, i - start + 1)

        return max_len


_cases = [
    (("abcabcbb",), 3),
    (("bbbbb",), 1),
    (("pwwkew",), 3),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol3(inputs, expected):
    sol = Solution()
    output = sol.lengthOfLongestSubstring(*inputs)
    assert output == expected
