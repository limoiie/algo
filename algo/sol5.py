# noinspection PyUnresolvedReferences
from typing import *

import pytest

# noinspection PyUnresolvedReferences
from algo.datatypes import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        start = 0

        palindromes = []
        for i, c in enumerate(s):
            next_palindromes = []
            palindromes.append(i)
            while palindromes:
                j = palindromes.pop()
                if j > 0 and c == s[j - 1]:
                    next_palindromes.append(j - 1)
                    if max_len < i - j + 2:
                        max_len = i - j + 2
                        start = j - 1
            palindromes = next_palindromes
            palindromes.append(i)
        return s[start : start + max_len]


_cases = [
    (("babad",), "bab"),
    (("cbbd",), "bb"),
    (("aacabdkacaa",), "aca"),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol5(inputs, expected):
    sol = Solution()
    output = sol.longestPalindrome(*inputs)
    assert output == expected
