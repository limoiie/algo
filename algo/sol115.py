from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sn = len(s)
        tn = len(t)
        dp = [[0] * (sn + 1) for _ in range(tn + 1)]
        for i in range(sn + 1):
            dp[0][i] = 1
        for i in range(1, tn + 1):
            for j in range(1, sn + 1):
                dp[i][j] = dp[i][j - 1]
                if t[i - 1] == s[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        return dp[tn][sn]


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=("rabbbit", "rabbit"), expected=3),
    TestCase(args=("babgbag", "bag"), expected=5),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.numDistinct(*case.args)
    assert output == case.expected
