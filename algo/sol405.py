from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def toHex(self, num: int) -> str:
        a = []
        chrs = "0123456789abcdef"
        for i in range(8):
            a.append(chrs[num & 0xF])
            num >>= 4
            if num == 0:
                break
        return "".join(reversed(a))


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(args=(26,), expected="1a"),
    TestCase(args=(-1,), expected="ffffffff"),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.toHex(*case.args)
    assert output == case.expected
