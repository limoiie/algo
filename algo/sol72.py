from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1) + 1, len(word2) + 1
        dp = [[math.inf] * n2 for _ in range(n1)]
        dp[0][0] = 0
        for i in range(n1):
            for j in range(n2):
                if i != 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                if j != 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
                if i != 0 and j != 0:
                    if word1[i - 1] == word2[j - 1]:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
                    else:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)
        return dp[n1 - 1][n2 - 1]


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(
        args=(
            "horse",
            "ros",
        ),
        expected=3,
    ),
    TestCase(
        args=(
            "intention",
            "execution",
        ),
        expected=5,
    ),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.minDistance(*case.args)
    assert output == case.expected
