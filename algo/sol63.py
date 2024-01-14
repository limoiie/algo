from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        if not obstacleGrid[0][0]:
            dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if not obstacleGrid[i][j]:
                    if i != 0:
                        dp[i][j] += dp[i - 1][j]
                    if j != 0:
                        dp[i][j] += dp[i][j - 1]
        return dp[m - 1][n - 1]


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([[0, 0, 0], [0, 1, 0], [0, 0, 0]],), expected=2),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.uniquePathsWithObstacles(*case.args)
    assert output == case.expected
