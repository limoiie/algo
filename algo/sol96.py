from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1, 1] + [0] * (n - 1)
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(1,), expected=1),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.numTrees(*case.args)
    assert output == case.expected
