from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1] + [0] * n
        for i in range(1, n + 1):
            if i > 0 and s[i - 1] != "0":
                dp[i] += dp[i - 1]
            if i > 1 and "10" <= s[i - 2 : i] <= "26":
                dp[i] += dp[i - 2]
        return dp[-1]


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=("12",), expected=2),
    TestCase(args=("226",), expected=3),
    TestCase(args=("06",), expected=0),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.numDecodings(*case.args)
    assert output == case.expected
