from algo import *


# noinspection PyPep8Naming,PyMethodMayBeStatic
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        for _ in range(32):
            r <<= 1
            if n & 1:
                r += 1
            n >>= 1
        return r


# leetcode submit region end(Prohibit modification and deletion)


_cases = [
    TestCase(
        args=(0b00000010100101000001111010011100,),
        expected=0b00111001011110000010100101000000,
    ),
    TestCase(
        args=(0b11111111111111111111111111111101,),
        expected=0b10111111111111111111111111111111,
    ),
]


@pytest.mark.parametrize("case", _cases)
def test_solution(case):
    sol = Solution()
    output = sol.reverseBits(*case.args)
    assert output == case.expected
