from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    dp: List[int]
    max_choosable_integer: int

    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger * (maxChoosableInteger + 1) < desiredTotal << 1:
            return False

        self.max_choosable_integer = maxChoosableInteger
        self.dp = [None] * (1 << (maxChoosableInteger + 1))

        return self.backtrace(0, desiredTotal)

    def backtrace(self, state, desiredTotal):
        if self.dp[state] is not None:
            return self.dp[state]

        self.dp[state] = False
        for i in range(1, self.max_choosable_integer + 1):
            if state & (1 << i) == 0:
                if i >= desiredTotal or not self.backtrace(
                    state | (1 << i), desiredTotal - i
                ):
                    self.dp[state] = True
                    break
        return self.dp[state]


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(...,), expected=...),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.canIWin(*case.args)
    assert output == case.expected
