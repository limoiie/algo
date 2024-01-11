from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 4095
        while True:
            if b == 0:
                return a if a <= 2048 else a - 4096
            a, b = a ^ b, (a & b) << 1
            a, b = a & mask, b & mask


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(-1, 1), expected=0),
    TestCase(args=(-2, 1), expected=-1),
    TestCase(args=(1, 2), expected=3),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.getSum(*case.args)
    assert output == case.expected
