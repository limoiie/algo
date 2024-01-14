import math

from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[math.inf] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i != 0:
                    dp[i][j] = min(dp[i - 1][j] + grid[i][j], dp[i][j])
                if j != 0:
                    dp[i][j] = min(dp[i][j - 1] + grid[i][j], dp[i][j])
        return dp[m - 1][n - 1]


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([[1, 3, 1], [1, 5, 1], [4, 2, 1]],), expected=7),
    TestCase(args=([[1, 2, 3], [4, 5, 6]],), expected=12),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.minPathSum(*case.args)
    assert output == case.expected
