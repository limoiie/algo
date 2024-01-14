from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        return dp[n]


def perm(n, k):
    return n * perm(n - 1, k - 1) if k > 0 else 1


dp = [1] * 9
for i in range(1, 9):
    dp[i] = dp[i - 1] + 9 * perm(9, i - 1)


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(0,), expected=1),
    TestCase(args=(2,), expected=91),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.countNumbersWithUniqueDigits(*case.args)
    assert output == case.expected
