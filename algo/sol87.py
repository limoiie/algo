from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        n = len(s1)
        dp = [[[None] * n for _ in range(n + 1)] for _ in range(n + 1)]

        def recur(ls, le, rs):
            if dp[ls][le][rs] is not None:
                return dp[ls][le][rs]
            if s1[ls:le] == s2[rs : rs + le - ls]:
                dp[ls][le][rs] = True
                return True
            for i in range(ls + 1, le):
                if (recur(ls, i, rs) and recur(i, le, rs + i - ls)) or (
                    recur(ls, i, rs + le - i) and recur(i, le, rs)
                ):
                    dp[ls][le][rs] = True
                    return True
            dp[ls][le][rs] = False
            return False

        return recur(ls=0, le=n, rs=0)


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=("great", "rgeat"), expected=True),
    TestCase(args=("abcde", "caebd"), expected=False),
    TestCase(args=("a", "a"), expected=True),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.isScramble(*case.args)
    assert output == case.expected
