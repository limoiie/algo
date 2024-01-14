from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        c = x ^ y
        count = 0
        while c:
            c = c & (c - 1)
            count += 1
        return count


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(1, 4), expected=2),
    TestCase(args=(3, 1), expected=1),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.hammingDistance(*case.args)
    assert output == case.expected
