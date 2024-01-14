from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2] + [0] * (n - 2)
        for k in range(3, n + 1):
            dp[k] = dp[k - 1] + dp[k - 2]
        return dp[n]


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(2,), expected=2),
    TestCase(args=(3,), expected=3),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.climbStairs(*case.args)
    assert output == case.expected
