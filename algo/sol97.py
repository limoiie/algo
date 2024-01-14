from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 + n2 != len(s3):
            return False

        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = True
        for i in range(n1 + 1):
            for j in range(n2 + 1):
                if i > 0 and s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
                if j > 0 and s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]:
                    dp[i][j] = dp[i][j] or dp[i][j - 1]
        return dp[-1][-1]


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(
        args=(
            "aabcc",
            "dbbca",
            "aadbbcbcac",
        ),
        expected=True,
    ),
    TestCase(
        args=(
            "aabcc",
            "dbbca",
            "aadbbbaccc",
        ),
        expected=False,
    ),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.isInterleave(*case.args)
    assert output == case.expected
