from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = i - 1
        for i in range(n):
            for j in range(0, min(i + 1, n - i)):
                if s[i - j] != s[i + j]:
                    break
                dp[i + j + 1] = min(dp[i + j + 1], dp[i - j] + 1)
            for j in range(1, min(i + 2, n - i)):
                if s[i - j + 1] != s[i + j]:
                    break
                dp[i + j + 1] = min(dp[i + j + 1], dp[i - j + 1] + 1)
        return dp[n]


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=("aab",), expected=1),
    TestCase(args=("a",), expected=0),
    TestCase(args=("ab",), expected=1),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.minCut(*case.args)
    assert output == case.expected
