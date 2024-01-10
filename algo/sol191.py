from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while n:
            if n & 1:
                c += 1
            n >>= 1
        return c


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(0b1011,), expected=3),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.hammingWeight(*case.args)
    assert output == case.expected
