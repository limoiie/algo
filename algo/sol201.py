from algo import *


# leetcode submit region begin(Prohibit modification and deletion)
# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right > left:
            right &= right - 1
        return right


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(...,), expected=...),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.rangeBitwiseAnd(*case.args)
    assert output == case.expected
