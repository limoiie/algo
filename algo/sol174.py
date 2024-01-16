from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[math.inf for _ in range(n + 1)] for _ in range(m + 1)]
        dp[m][n - 1] = dp[m - 1][n] = 1

        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)
        return dp[0][0]


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]],), expected=7),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.calculateMinimumHP(*case.args)
    assert output == case.expected
