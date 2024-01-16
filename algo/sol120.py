from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0] * (i + 1) for i in range(len(triangle))]
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
            dp[i][-1] = dp[i - 1][-1] + triangle[i][-1]
        return min(dp[-1])


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]],), expected=11),
    TestCase(args=([[-10]],), expected=-10),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.minimumTotal(*case.args)
    assert output == case.expected
