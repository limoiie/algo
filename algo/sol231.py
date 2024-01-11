from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(1,), expected=True),
    TestCase(args=(2,), expected=True),
    TestCase(args=(4,), expected=True),
    TestCase(args=(16,), expected=True),
    TestCase(args=(0,), expected=False),
    TestCase(args=(3,), expected=False),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.isPowerOfTwo(*case.args)
    assert output == case.expected
