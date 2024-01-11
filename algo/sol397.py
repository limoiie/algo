from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def integerReplacement(self, n: int) -> int:
        ans = 0
        while n != 1:
            if n & 1 == 0:
                n >>= 1
            elif n == 3 or (n >> 1) & 1 == 0:
                n -= 1
            else:
                n += 1
            ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(8,), expected=3),
    TestCase(args=(7,), expected=4),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.integerReplacement(*case.args)
    assert output == case.expected
