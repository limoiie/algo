from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0 and count_bits(n) % 2 == 1


def count_bits(n: int):
    cnt = 0
    while n:
        cnt += 1
        n >>= 1
    return cnt


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(16,), expected=True),
    TestCase(args=(5,), expected=False),
    TestCase(args=(1,), expected=True),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.isPowerOfFour(*case.args)
    assert output == case.expected
