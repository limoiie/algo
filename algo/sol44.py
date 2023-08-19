import pytest


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[0][0] = True

        for pi, pc in enumerate(p):
            if pc == "*":
                for si in range(len(s) + 1):
                    if dp[pi][si]:
                        dp[pi + 1][si] = True
                        while si < len(s):
                            dp[pi + 1][si + 1] = True
                            si += 1
                        break

            elif pc == "?":
                for si, sc in enumerate(s):
                    if dp[pi][si]:
                        dp[pi + 1][si + 1] = True

            else:
                for si, sc in enumerate(s):
                    if dp[pi][si] and sc == pc:
                        dp[pi + 1][si + 1] = True

        return dp[-1][-1]


_cases = [
    (("aa", "a"), False),
    (("aa", "*"), True),
    (("cb", "?a"), False),
    (("", "*"), True),
    (("", "****"), True),
    (("b", "*?*?*"), False),
    (("de", "de*"), True),
    (("de", "de***"), True),
]


@pytest.mark.parametrize("inputs,expected", _cases)
def test_sol44(inputs, expected):
    sol = Solution()
    output = sol.isMatch(*inputs)
    assert output == expected
