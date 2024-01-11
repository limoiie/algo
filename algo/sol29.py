from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def divide(self, dividend: int, divider: int) -> int:
        if dividend == -2147483648 and divider == -1:
            return 2147483647
        a, b, res = abs(dividend), abs(divider), 0
        for x in range(32)[::-1]:
            if (a >> x) - b >= 0:
                res += 1 << x
                a -= b << x
        return res if (dividend > 0) == (divider > 0) else -res


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(...,), expected=...),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.divide(*case.args)
    assert output == case.expected
